# Troubleshooting your Safari web extension

**Framework**: Safari Services

Use developer resources to investigate and resolve common problems with Safari web extensions.

#### Overview

When you experience issues with your Safari web extension, choose the right developer tool or resource to troubleshoot and resolve the issue, based on the type of issue you experience.

##### Install and Enable the Extension in Safari

If you’re not able to see your extension running in Safari when you expect, try these steps to install and enable your extension.

- Build and run your Safari web extension. You need to run the containing macOS or iOS app for your extension at least once to install it in Safari. For more information, see [`Running your Safari web extension`](running-your-safari-web-extension.md).
- Enable the Safari web extension in macOS. Open Safari and choose Safari > Settings. Select the Extensions tab, find your extension, and select its checkbox. If you’re developing your extension and it isn’t visible in Safari Settings, you need to allow unsigned extensions in Safari. For more information, see [`Configure Safari in macOS to run unsigned extensions`](running-your-safari-web-extension#Configure-Safari-in-macOS-to-run-unsigned-extensions.md).
- Enable the Safari web extension in iOS. In Safari, tap the More menu, then tap Extensions to select and enable your extension. Alternatively, open the Settings app, then choose Safari > Extensions. Find your extension in the list, tap it, then tap the switch to enable it, if necessary.
- Enable the Safari web extension for a profile in Safari 17 and later. In macOS, choose Safari > Settings, click the Profiles tab, select a profile, and then click the Extensions tab to manage the permission status for each extension for a profile. In iOS, open the Settings app, then select a profile in the Profiles group, and toggle permission for that profile’s available extensions.
- Enable the Safari web extension in a Mac web app in macOS 15 and later. In the Mac web app, choose Settings from the menu. Select the Extensions tab, find your extension, and select its checkbox. If you’re developing your extension and it isn’t visible in the web app’s settings, you need to allow unsigned extensions for the web app. For more information, see [`Configure Safari in macOS to run unsigned extensions`](running-your-safari-web-extension#Configure-Safari-in-macOS-to-run-unsigned-extensions.md).
- Compare your deployment target to your system version.

To compare your deployment target to your system version, you need to check the deployment target for both your app and the extension targets (for both macOS and iOS, if applicable):

1. Choose  > About This Mac to get your macOS system version number. In iOS, open the Settings app, and choose General > About to see the software version.
2. In Xcode, select your web extension project in the Project navigator pane to see the project editor.
3. Select the app or extension target under the Targets section.
4. Select the General pane, then find the deployment target version number in the Deployment Info section.

Check that the deployment targets for your app and extension are the same, and are earlier than or the same as the version of the system you’re testing on. If not, lower the deployment targets or update your system, if possible. Note that your project may encounter errors if you set the deployment target below the minimum level required to support features in your extension.

After you complete these steps for macOS, verify that Safari sees your extension. In the Terminal app, type the following command to see a list of installed extensions:

```other
pluginkit -mAvvv -p com.apple.Safari.web-extension
```

If your extension is installed and visible to Safari, the command lists information about it. If it isn’t visible, recheck the other steps above.

##### Enable Safaris Develop Menu

Use Safari’s macOS developer tools to gain insight into your extension and debug issues. In Safari, choose Safari > Settings, click Advanced, and then select the “Show Develop menu in menu bar” option at the bottom. Safari adds a Develop menu item with a number of useful inspectors and [`web development tools`](https://developer.apple.comhttps://developer.apple.com/safari/tools/).

After you enable the Develop menu, Control-click any element and select Inspect Element to see it in the Elements inspector.

To use Safari’s Web Inspector for iOS, first enable the Web Inspector on your device. Open the Settings app, then choose Safari > Advanced. Find the Web Inspector item, then tap the switch to enable it. Attach your device to your computer with a cable, and access your device from the Develop menu in Safari on your computer.

##### Debug Your Content and Background Scripts

Safari’s developer tools include a debugger that you can use to debug scripts in your Safari web extension.

To debug your JavaScript content scripts in macOS, choose Develop > Show Web Inspector from the Safari menu bar. In iOS, have a simulator open with your extension or attach your iOS device to your computer, then select your simulator or device from Safari’s Develop menu on your computer, and select the page with your extension. Click the Sources tab, and select your content script file from the Extension Scripts folder at the lower left. Then select your extension’s execution context by using the selector in the lower-right corner of the inspector. Set breakpoints by clicking the gutter with line numbers in the source view. Inspect other source files for your extension, such as style sheets, in the Sources area at the lower left.

![A screenshot that shows the Safari web inspector view, showing a selected content script file in the Sources tab with a breakpoint set.](https://docs-assets.developer.apple.com/published/6b0c1c8291dc6787d5d21d5d631bda66/media-3734526%402x.png)

To debug background scripts in macOS, choose Develop > Web Extension Background Pages and select your background script. In Safari 17 and later in macOS, choose Develop > Web Extension Background Content, then select your background script and profile. In iOS, connect the device to a Mac. In Safari on the Mac, choose Develop > Device, and then select the item containing your extension name, “Extension Background Page,” and the filename of your background script.

To debug your extension’s pop-up in macOS, click the button for your extension in the Safari toolbar to display the pop-up. Control-click the pop-up and select Inspect Element to display the Web Inspector for the pop-up. In iOS, connect the device to a Mac. In Safari on the Mac, choose Develop > Device, and then select the item containing your extension name, “Extension Popup Page,” and the filename of your pop-up’s HTML.

##### Log Messages to the System Console

If you’re having issues messaging between your native app and your web extension in macOS, log messages to the system console to perform basic debugging. See [`Diagnosing and resolving bugs in your running app`](https://developer.apple.com/documentation/Xcode/diagnosing-and-resolving-bugs-in-your-running-app) to use Xcode’s debugger to inspect your native app when you need more comprehensive debugging tools.

In the native part of the macOS or iOS app or extension, make calls to `NSLog` (for Objective-C) or `print` (for Swift) to log messages in the system console, and view them in Console.app.

In Console.app, filter for other messages using the name of your app extension. For example, if the system terminates your app extension because of an error, it sends a message to the console and generates a crash log.

##### Check Permissions and Compatibility

When your web extension works on one webpage, but doesn’t work on another, make sure your website access permissions and allowed domain patterns are correct. For more information, see Mozilla’s match pattern documentation at [`Match patterns in extension manifests`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns).

When your web extension works in another browser, but doesn’t work in Safari, check for potential compatibility issues. Review your `manifest.json` keys and JavaScript APIs to confirm that Safari supports them. If Safari doesn’t support them, implement the recommended workaround. For more information, see [`Assessing your Safari web extension’s browser compatibility`](assessing-your-safari-web-extension-s-browser-compatibility.md).

## See Also

- [Optimizing your web extension for Safari](optimizing-your-web-extension-for-safari.md)
  Support Dark Mode, reduce memory and power usage, and ensure feature compatibility to improve your web extension experience in Safari and web apps.
- [Adopting New Safari Web Extension APIs](adopting-new-safari-web-extension-apis.md)
  Improve your web extension in Safari with a non-persistent background page and new tab-override customization.
- [Syncing Safari web extensions across devices and platforms](syncing-safari-web-extensions-across-devices-and-platforms.md)
  Let users install your extension on one device and then use and manage the extension on all their other iOS and macOS devices.
- [Assessing your Safari web extension’s browser compatibility](assessing-your-safari-web-extension-s-browser-compatibility.md)
  Review your Safari web extension implementation plan, manifest keys, and JavaScript API usage for compatibility with other browsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/troubleshooting-your-safari-web-extension)*