# Messaging between the app and JavaScript in a Safari web extension

**Framework**: Safari Services

Communicate about events and share data between the containing app and JavaScript by using native messaging and app groups.

#### Overview

A Safari web extension consists of three parts that operate independently in their own sandboxed environments:

- A macOS or iOS app that can have a user interface
- JavaScript code and web files that work in the browser or Mac web app
- A native app extension that mediates between the macOS or iOS app and the JavaScript code

You use messaging APIs to communicate events and event data between these parts. You use app groups to share app data between them.

Because the macOS or iOS app and the native app extension each run in their own sandboxed environments, they cannot share data in their respective containers. You can store data in a shared space that both the macOS or iOS app and the native app extension can access and update, by enabling app groups. For more information, see [`Sharing Data with Your Containing App`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionScenarios.html#//apple_ref/doc/uid/TP40014214-CH21-SW6).

##### Send Messages From Javascript to the App

You can send messages to the native app extension from a background script or from extension pages that provide a user interface for your Safari web extension. Content scripts that are injected into web content cannot send messages to the native app extension.

To enable sending messages from JavaScript to the native app extension, add `nativeMessaging` to the list of `permissions` in the `manifest.json` file.

From a script running in the browser or Mac web app, use `browser.runtime.sendNativeMessage` to send a message to the native app extension:

```javascript
browser.runtime.sendNativeMessage("application.id", {message: "Hello from background page"}, function(response) {
    console.log("Received sendNativeMessage response:");
    console.log(response);
});
```

Safari ignores the `application.id` parameter and only sends the message to the containing app’s native app extension. To receive the message, implement the `beginRequest:with:` function in the native app extension to handle the message:

```swift
func beginRequest(with context: NSExtensionContext) {
        guard let item = context.inputItems.first as? NSExtensionItem,
              let userInfo = item.userInfo as? [String: Any],
              let message = userInfo[SFExtensionMessageKey] else {
            context.completeRequest(returningItems: nil, completionHandler: nil)
            return
        }

        if let profileIdentifier = userInfo[SFExtensionProfileKey] as? UUID {
            // Perform profile specific tasks.
        } else {
            // Perform normal browsing tasks.
        }

        let response = NSExtensionItem()
        response.userInfo = [ SFExtensionMessageKey: [ "Response to": message ] ]
            
        context.completeRequest(returningItems: [response], completionHandler: nil)
}
```

The message from the script is the first item in the `context.inputItems` dictionary using [`SFExtensionMessageKey`](sfextensionmessagekey.md) as the key. In Safari 17 or later, get the profile identifier from the `context.inputItems` dictionary using [`SFExtensionProfileKey`](sfextensionprofilekey.md) as the key. Use the profile identifier for any extension logic that you need to limit to the user’s profile or to a web app instance, such as fetching or storing data.

Reply to the message by creating an `NSExtensionItem` response, populating response data in `userInfo`, and calling `context.completeResponse:returningItems:completionHandler` with the response.

##### Send Messages From the App to Javascript

To enable sending messages from the Safari web extension’s containing macOS app to its JavaScript scripts running in the browser or Mac web app, add `nativeMessaging` to the list of `permissions` in the `manifest.json` file. Send messages from the macOS app to notify the web scripts of important events, like when the user clicks a button or when data that the JavaScript script uses changes. You can’t send messages from a containing iOS app to your web extension’s JavaScript scripts.

To prepare the JavaScript script to receive messages from the macOS app, use `browser.runtime.connectNative` to establish a port connection to the containing app:

```javascript
let port = browser.runtime.connectNative("application.id");
```

Safari ignores the `application.id` parameter and only allows the script to establish a port connection with the containing macOS app.

Send a message to the JavaScript script from the macOS app using `dispatchMessageWithName:toExtensionWithIdentifier:userInfo` in `SFSafariApplication`:

```swift
@IBAction func sendMessageToExtension(_ sender: AnyObject?) {
    let messageName = "Hello from App"
    let messageInfo = ["AdditionalInformation":"Goes Here"]
    SFSafariApplication.dispatchMessage(withName: messageName, toExtensionWithIdentifier: extensionBundleIdentifier, userInfo: messageInfo) { error in
        debugPrint("Message attempted. Error info: \(String.init(describing: error))")
    }
}
```

To receive the message in the JavaScript script, add a closure using `port.onMessage.addListener` to process the message.

```javascript
port.onMessage.addListener(function(message) {
    console.log("Received native port message:");
    console.log(message);
});
```

The script then processes the message and initiates events in the browser.

## See Also

- [let SFExtensionMessageKey: String](sfextensionmessagekey.md)
  A string the system uses as a key in a user info dictionary to identify a message.
- [let SFExtensionProfileKey: String](sfextensionprofilekey.md)
  A string the system uses as a key in a user info dictionary to identify a profile identifier.
- [Messaging a Web Extension’s Native App](messaging-a-web-extension-s-native-app.md)
  Communicate between your Safari web extension and its containing app.
- [Messaging between a webpage and your Safari web extension](messaging-between-a-webpage-and-your-safari-web-extension.md)
  Configure your extension to enable messaging from webpages, and then update your extension to handle messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/messaging-between-the-app-and-javascript-in-a-safari-web-extension)*