# Injecting CSS style sheets into a webpage

**Framework**: Safariservices

Add to or override styles by injecting CSS style sheets into webpages.

#### Overview

After you write a style sheet that can modify page presentation, you need to add it to your Safari app extension and apply it to webpages.

A style sheet can apply to a single webpage, all webpages, or only some webpages — for example, webpages from certain domains. To inject your style sheet, you specify either `Some` or `All` website access for your app extension. In Safari 17 or later, users also need to grant your extension access to a website. For more information, see [`Adjusting website access permissions`](adjusting-website-access-permissions.md). For more information about injected style sheets, see [`Using injected style sheets and scripts`](using-injected-style-sheets-and-scripts.md).

##### Add a Style Sheet

After specifying website access, add the style sheet to your Safari app extension.

1. Add the CSS files to your extension’s Xcode target.
2. Add an `SFSafariStyleSheet` key to the `NSExtension` element in your extension’s `Info.plist` file. The value for this key is an array of dictionaries.
3. For each CSS file, add a dictionary to this array. Each dictionary must have a `Style Sheet` key with a value that specifies the path (relative to the Resources directory of the bundle) to the style sheet to include.

> **Note**:  By default, the system injects a style sheet when the extension has permission to access the webpage. However, you can specify additional dictionary keys to provide more fine-grained control over whether to inject that style sheet into the webpage. For more information, see Access and permissions.

You can have more than one injected style sheet. Style sheets process in the order in which you specify them.

Your style sheet can reference resources in your app extension’s bundle. All relative URLs are relative to the Resources folder in the app extension’s bundle.

## See Also

- [Using injected style sheets and scripts](using-injected-style-sheets-and-scripts.md)
  Learn how you can affect the appearance or behavior of a webpage by using injected style sheets and scripts.
- [Injecting a script into a webpage](injecting-a-script-into-a-webpage.md)
  Inject a script that you write for a Safari app extension into a webpage.
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

*[View on Apple Developer](https://developer.apple.com/documentation/SafariServices/injecting-css-style-sheets-into-a-webpage)*