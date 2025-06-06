# Injecting a script into a webpage

**Framework**: Safari Services

Inject a script that you write for a Safari app extension into a webpage.

#### Overview

After you write a script that can read and modify browser content, you need to add it to your Safari app extension and apply it to webpages, where it can perform the defined actions and change the appearance and behavior of the webpages.

A script can apply to a single webpage, all webpages, or only some webpages — for example, webpages from certain domains. To inject your script, you specify either `Some` or `All` website access for your app extension. In Safari 17 or later, users also need to grant your extension access to a website. For more information, see [`Adjusting website access permissions`](adjusting-website-access-permissions.md). For more information about injected scripts, see [`Using injected style sheets and scripts`](using-injected-style-sheets-and-scripts.md).

##### Add a Script

After specifying website access, add the script to your Safari app extension.

1. Add the script files to your extension’s Xcode target.
2. Add an `SFSafariContentScript` key to the `NSExtension` element in your extension’s `Info.plist` file. The value for this key is an array of dictionaries.
3. For each script file, add a dictionary to the array. Each dictionary must have a `Script` key with a value that specifies the path (relative to the Resources directory of the bundle) to the script file to include.

> **Note**:  By default, the system injects a script file when the extension has permission to access the webpage. However, you can specify additional dictionary keys to provide more fine-grained control over whether to inject that script file into the webpage. For more information, see Access and permissions.

 By default, the system injects a script file when the extension has permission to access the webpage. However, you can specify additional dictionary keys to provide more fine-grained control over whether to inject that script file into the webpage. For more information, see Access and permissions.

If your app extension specifies multiple scripts to inject into the webpage, the scripts execute in the order in which they appear in the `Info.plist` file.

##### Access Resources Within Your App Extensions Bundle

To access the resources in your app extension’s bundle from within your scripts, create a URL at runtime that references the resource relative to the root of the app extension’s bundle. The `safari.extension.baseURI` property specifies the location of the bundle’s resource directory.

The code example below demonstrates how to use this property. This code adds a new image element to the webpage. The system stores the image inside the Resources folder and references it at runtime.

```javascript
var newElement = document.createElement("img");
newElement.src = safari.extension.baseURI + "myDog.jpeg";
```

##### Execute Your Code After the Webpage Loads

The injected scripts execute before the webpage fully loads, so you can take action as the system adds resources to the webpage. During that time, `document.body` is `null`. To take action after the document loads, listen for the `DOMContentLoaded` event. The code example below registers a document event handler to call after the content loads:

```javascript
document.addEventListener("DOMContentLoaded", function(event) {
    safari.extension.dispatchMessage("Hello World!");
});
```

##### Add an Element to the Webpage

The example code below injects a new element into the webpage after the webpage loads. This example uses a resource stored in the bundle and shows how to register the document event handler:

```swift
// Create an image and insert it at the top of the body.
document.addEventListener("DOMContentLoaded", function(event) {
    var newElement = document.createElement("img");
    newElement.src = safari.extension.baseURI + "myCat.jpg";
    document.body.insertBefore(newElement,
    document.body.firstChild);
});
```

## See Also

- [Using injected style sheets and scripts](using-injected-style-sheets-and-scripts.md)
  Learn how you can affect the appearance or behavior of a webpage by using injected style sheets and scripts.
- [Injecting CSS style sheets into a webpage](injecting-css-style-sheets-into-a-webpage.md)
  Add to or override styles by injecting CSS style sheets into webpages.
- [Passing messages between Safari app extensions and injected scripts](passing-messages-between-safari-app-extensions-and-injected-scripts.md)
  Communicate between your Safari app extension and injected scripts.
- [class SFSafariExtensionHandler](sfsafariextensionhandler.md)
  A base class that you subclass to handle events in your Safari app extension.
- [class SFSafariExtensionManager](sfsafariextensionmanager.md)
  A class that your app uses to find out the current state of a Safari app extension.
- [class SFSafariExtensionState](sfsafariextensionstate.md)
  The state of a Safari app extension.
- [class SFSafariPageProperties](sfsafaripageproperties.md)
  An object that captures information about a webpage.
- [protocol SFSafariExtensionHandling](sfsafariextensionhandling.md)
  A protocol for implementing event handling in a Safari app extension.
- [let SFExtensionProfileKey: String](sfextensionprofilekey.md)
  A string the system uses as a key in a user info dictionary to identify a profile identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/injecting-a-script-into-a-webpage)*