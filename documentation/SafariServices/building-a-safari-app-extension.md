# Building a Safari app extension

**Framework**: Safari Services

Add, build, and enable a Safari app extension.

#### Overview

You deliver a Safari app extension inside a macOS app. When a user runs your app for the first time, the app extension immediately becomes available in Safari. This article explains the following steps to build your own Safari app extension:

1. Adding a Safari app extension target to your app in Xcode.
2. Adding script and style sheet files to inject into your app and modify webpage content.
3. Adjusting property list values in your app that relate to the Safari app extension.
4. Building and running your app, which builds your Safari app extension for use.
5. Enabling your Safari app extension in Safari so you can use it.

##### Add a Safari App Extension Target in Xcode

To create a Safari app extension:

1. Launch Xcode and either open an existing project containing a macOS app or create a new one.
2. Choose File > New > Target.
3. From the list of templates in the Application Extension section, select Safari Extension, and click Next.
4. Enter a product name for your extension, such as .
5. From the Type menu, choose Safari App Extension.
6. Make sure that your app project is selected in the Project menu, and that your macOS app target is selected in the Embed in Application menu.
7. Click Finish.
8. If Xcode asks you if you want to activate a new scheme for your new extension, click Cancel.

Xcode adds a new group into your project, which contains several new files, including an `Info.plist` file, a variety of supporting source files, an Interface Builder file, a JavaScript file, and a toolbar image PDF.

##### Add Scripts and Style Sheets

After you add scripts and style sheets to your Safari app extension, you can read and modify webpage content, and read and send data from your app. For more information about injecting scripts and style sheets into your webpage content, see [`Using injected style sheets and scripts`](using-injected-style-sheets-and-scripts.md).

##### Add Keys to the Information Property List Template

The default `Info.plist` file identifies your new Safari app extension and specifies its capabilities and access limits under the `NSExtension` key. For more information about setting these capabilities and limits, see [`Safari app extension information property list keys`](safari-app-extension-information-property-list-keys.md). In your information property list file, you can also specify custom UI options, like contextual menu items and toolbar items. For more information about these settings, see [`Using contextual menu and toolbar item keys`](using-contextual-menu-and-toolbar-item-keys.md).

##### Build and Run the App

Before Safari can find your new extension, you must run the containing app at least once:

1. Make sure that your macOS app is selected in the Scheme menu in Xcode’s main toolbar.
2. Click the Run button, or choose Product > Run to build and run your app.

When you build your app, Xcode builds your Safari app extension first, then embeds it inside the finished app bundle. As soon as your app runs, your extension is ready for use in Safari.

##### Enable Your App Extension in Safari

If you’re not part of the Apple Development Program, or if you don’t have a developer identity for your existing Xcode project, Xcode can’t sign your Safari app extension with a development certificate. For security purposes, Safari, by default,  ignores unsigned extensions, so your extension doesn’t appear in Safari Extensions settings.

To develop without a certificate, each time you launch Safari, you need to tell it to load unsigned extensions using the Develop menu:

1. Open Safari and choose Safari > Settings.
2. Select the Advanced tab, then select the “Show Develop menu in menu bar” checkbox.
3. Choose Develop > Allow Unsigned Extensions, enter your password, and click OK. If you’re using Safari 17 or later, click the Developer tab in Safari Settings, and select the “Allow unsigned extensions” option. The Allow Unsigned Extensions setting resets when a user quits Safari, so you need to set it again the next time you launch Safari.
4. Choose Safari > Settings and click the Extensions tab. This tab shows the localized description, display name, and version number for the selected Safari app extension. It also provides a more nuanced message about the permissions for the extension.
5. Find your new extension in the list on the left, and enable it by selecting its checkbox.
6. Close Safari Settings.

In Safari 17 and later, the user can also toggle permission for the extension overall, in Private Browsing, or for each profile. If the user has profiles set up, they can choose Safari > Settings, click the Profiles tab, select a profile, and then click the Extensions tab to manage whether each extension is enabled for a profile.

If you build the default template extension without modifying it, a new toolbar item (a button) appears in the Safari toolbar. When you click this button, the Safari app extension logs a message that you can view in the system console — this message comes from your [`SFSafariExtensionHandler`](sfsafariextensionhandler.md) subclass.

If you have trouble getting your extension to work, see [`Troubleshooting your Safari app extension`](troubleshooting-your-safari-app-extension.md).

## See Also

- [Converting a legacy Safari extension to a Safari app extension](converting-a-legacy-safari-extension-to-a-safari-app-extension.md)
  Convert a legacy Safari extension to a Safari app extension, automatically with keys or manually.
- [Troubleshooting your Safari app extension](troubleshooting-your-safari-app-extension.md)
  Debug your Safari app extension with these techniques.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/building-a-safari-app-extension)*