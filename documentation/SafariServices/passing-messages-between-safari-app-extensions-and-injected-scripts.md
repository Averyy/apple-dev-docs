# Passing messages between Safari app extensions and injected scripts

**Framework**: Safari Services

Communicate between your Safari app extension and injected scripts.

#### Overview

The injected script and your Safari app extension live in different sandboxed worlds, each with specific limits on what it can access. You can’t call directly from the native code in your app extension to the injected script running in the browser. However, some sort of communication between the two is almost always desirable. For example, you may have a toolbar or contextual menu item that you want to use to affect web content.

The solution is to pass messages between the injected script and the app extension. The two runtime environments share a common format for message passing, and each provides an interface for sending and receiving messages.

The complete workflow appears below:

![A diagram showing a message passing from a Safari app extension to an injected script in a webpage and back to the app extension. ](https://docs-assets.developer.apple.com/published/8936272251b5d55a7116403b63e2c45d/media-3027374%402x.png)

Within the scripting environment, you have access to the `window` and `document` objects for the browser content, as well as a `safari` object. The `safari` object is an instance of the `SafariAppExtensionNamespace` class. It provides details about your app extension and support for passing messages between your injected script and the app extension.

This table describes your app extension’s key properties:

| Property | Description |
| --- | --- |
| `extension` | A proxy for the app extension. Use it to retrieve information about your app extension and to pass messages to it. |
| `self` | A proxy for your injected script. Use it to install event listeners to respond to messages from your app extension. |

##### Send Messages to the App Extension

Call `safari.extension.dispatchMessage.`

```javascript
safari.extension.dispatchMessage("Hello World");

```

The parameter for [`dispatchMessage`](https://developer.apple.com/documentation/safariextensions/safariappextension/2048642-dispatchmessage) is a string that identifies the message you want to send. You create your own message names and decide what those messages mean for your app extension.

You can optionally send additional user data to accompany the message.

```javascript
safari.extension.dispatchMessage("InterestingMessage",  { "key": "value" });
```

The user data must be a JavaScript object made up of keys and values that conform to the W3C standard for safe passing of structured data, such as Boolean objects, numeric values, strings, arrays, and so on.

For example, the following code sends an array in a message:

```javascript
var myArray = ["a", "b", "c"];
safari.extension.dispatchMessage("passArray", { "key": myArray });
```

When the app extension receives the message, the system calls the extension handler’s [`messageReceived(withName:from:userInfo:)`](sfsafariextensionhandling/messagereceived(withname:from:userinfo:).md) method. This method’s parameters include the message name, the page that sends the message, and, if part of the message, a user dictionary:

In Safari 17 and later, check whether the user is browsing with a profile if you need to limit any extension logic to the profile, such as fetching or storing data. To do that, implement the [`beginRequest(with:)`](https://developer.apple.com/documentation/Foundation/NSExtensionRequestHandling/beginRequest(with:)) method.

```swift
- (void)beginRequestWithExtensionContext:(NSExtensionContext *)context {
    NSExtensionItem *item = context.inputItems.firstObject;
    NSDictionary *userInfo = item.userInfo;
    NSUUID *profileIdentifier = userInfo[SFExtensionProfileKey];
    
    if (profileIdentifier != nil) {
        // Remember profile identifier for future method calls.
    } else {
        // Handle normal browsing. 
    }
}
```

Then, get the profile identifier from the `context.inputItems` dictionary using [`SFExtensionProfileKey`](sfextensionprofilekey.md) as the key. Use the profile identifier for any profile-specific logic.

##### Send Messages to the Injected Script

When the app extension needs to send a message to an injected script, it calls the [`dispatchMessageToScript(withName:userInfo:)`](sfsafaripage/dispatchmessagetoscript(withname:userinfo:).md) method on the target page.

The message is a packaged event with a type of `message`. To respond to the message, the injected script registers an event listener for message events using `safari.self.addEventListener.`

```swift
safari.self.addEventListener("message", handleMessage);

```

The event that passes into the event handler is a `SafariExtensionMessageEvent` object. Its `name` property identifies the message, and its `message` property contains the dictionary of user data.

```javascript
function handleMessage(event) {
    console.log(event.name);
    console.log(event.message);
}
```

## See Also

- [Using injected style sheets and scripts](using-injected-style-sheets-and-scripts.md)
  Learn how you can affect the appearance or behavior of a webpage by using injected style sheets and scripts.
- [Injecting a script into a webpage](injecting-a-script-into-a-webpage.md)
  Inject a script that you write for a Safari app extension into a webpage.
- [Injecting CSS style sheets into a webpage](injecting-css-style-sheets-into-a-webpage.md)
  Add to or override styles by injecting CSS style sheets into webpages.
- [class SFSafariExtensionHandler](sfsafariextensionhandler.md)
  A base class that you subclass to handle events in your Safari app extension.
- [class SFSafariExtensionManager](sfsafariextensionmanager.md)
  A class that your app uses to find out the current state of a Safari extension.
- [class SFSafariExtensionState](sfsafariextensionstate.md)
  The state of a Safari extension.
- [class SFSafariPageProperties](sfsafaripageproperties.md)
  An object that captures information about a webpage.
- [protocol SFSafariExtensionHandling](sfsafariextensionhandling.md)
  A protocol for implementing event handling in a Safari app extension.
- [let SFExtensionProfileKey: String](sfextensionprofilekey.md)
  A string the system uses as a key in a user info dictionary to identify a profile identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/passing-messages-between-safari-app-extensions-and-injected-scripts)*