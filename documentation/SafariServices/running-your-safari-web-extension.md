# Running your Safari web extension

**Framework**: Safari Services

Install and update your extension in Safari as you make changes in development.

#### Overview

Install your web extension in Safari, then update it as you add features and fix bugs so you can run and test it in Safari.

You can temporarily install your extension folder in macOS Safari for testing without setting up an Xcode project. Use this approach to quickly evaluate your extension in Safari or to complete your initial development work. Then, when you’re ready to test your extension in iOS or distribute your extension, follow the instructions in [`Converting a web extension for Safari`](converting-a-web-extension-for-safari.md) to create an Xcode project.

##### Temporarily Install a Web Extension Folder in Macos Safari

To temporarily install your web extension folder in macOS Safari, first locate the folder or zip file containing your web extension’s files in Finder, then open Safari.

1. In the Safari menu, choose Safari > Settings.
2. Select the Developer tab. If it’s not visible, see [`Configure Safari in macOS to run unsigned extensions`](running-your-safari-web-extension#Configure-Safari-in-macOS-to-run-unsigned-extensions.md) below to enable it.
3. Click “Add Temporary Extension…”, then respond to Safari’s unsigned extension authentication prompt, if you haven’t already selected the “Allow unsigned extensions” option.
4. Select the folder or zip file containing your web extension files, and click Select.

If your folder contains a valid web extension, Safari switches to the Extensions tab and adds your extension to the Temporary list. Use the options to uninstall the extension, adjust the extension’s settings, show the extension in Finder, or reload the extension in Safari.

Safari removes temporary extensions after 24 hours or when you quit Safari.

> ❗ **Important**: Set up your extension in an Xcode project to test your web extension in iOS, send messages between the extension and your app, or distribute your extension. For more information, see [`Converting a web extension for Safari`](converting-a-web-extension-for-safari.md).

##### Install Your Safari Web Extension in Ios

If you’re working in iOS, you deploy a Safari web extension in Safari with an iOS app. If you are testing on a device, attach your development iOS device to your computer, then run the containing iOS app to install your web extension in Safari:

1. Select the iOS app in the Scheme menu next to the Run and Stop buttons in Xcode’s main toolbar.
2. Select your development device or preferred iOS simulator in the Device menu next to the Scheme menu.
3. Click the Run button, or choose Product > Run to build and run your app.

Xcode builds your Safari web extension first, then embeds it inside the finished app bundle. Xcode then deploys the app to your development device or selected simulator.

When you install the app in iOS for the first time, enable the web extension in Safari before you run it. In Safari, tap the More menu, then tap Extensions to select and enable your extension. Alternatively, open the Settings app, then select Safari > Extensions. Find your extension in the list, tap it, then tap the switch to enable the extension.

> **Note**:  You must be a member of the [`Apple Developer Program`](https://developer.apple.comhttps://developer.apple.com/programs/) to test on a device. You can test in the iOS simulators before you join the Apple Developer Program.

##### Install Your Safari Web Extension in Macos

If you’re working in macOS, you use a macOS app to deploy a Safari web extension. Run the containing macOS app to install your web extension in Safari:

1. Select the macOS app in the Scheme menu next to the Run and Stop buttons in Xcode’s main toolbar.
2. Click the Run button, or choose Product > Run to build and run your app.

When you build your app, Xcode builds your Safari web extension first, then embeds it inside the finished app bundle. As soon as your app runs, your extension is ready for use in Safari.

##### Configure Safari in Macos to Run Unsigned Extensions

If you’re not part of the Apple Developer Program, or if you haven’t yet configured a developer identity for your existing Xcode project, your Safari web extension won’t be signed with a development certificate. For security purposes, Safari ignores unsigned extensions by default, so your extension won’t show up in Safari Extensions preferences.

To develop without a certificate, allow unsigned extensions in Safari. First, enable the Develop menu in Safari:

1. Choose Safari > Settings.
2. Select the Advanced tab.
3. Check the “Show Develop menu in menu bar” box, or the “Show features for web developers” box in Safari 17 or later.

Then, in Safari 16 and earlier, choose Develop > Allow Unsigned Extensions. In Safari 17 or later, use the Developer tab in Settings:

1. Choose Safari > Settings.
2. Select the Developer tab.
3. Check the “Allow unsigned extensions” box.

The “Allow unsigned extensions” setting for Safari resets when you quit Safari; set it again the next time you launch Safari.

In a Mac web app:

1. Choose Settings from the Mac web app’s menu.
2. Select the Extensions tab.
3. Check the “Allow unsigned extensions” box.

The “Allow unsigned extensions” setting resets for the web app when you quit that web app; set it again the next time you launch the web app.

Now enable your extension:

1. Choose Safari > Settings, or Settings from the Mac web app’s menu.
2. Select the Extensions tab.  This tab shows the localized description, display name, and version number for the selected extension. It also provides more information about the permissions claimed by the extension.
3. Find your new extension in the list on the left, and enable it by selecting the checkbox.
4. Close Settings.

If you have profiles set up in Safari 17 or later, manage your extension for a specific profile:

1. Choose Safari > Settings.
2. Select the Profiles tab.
3. Select a profile.
4. Select the Extensions tab.

If you built the default template extension without modifying it, Safari adds a button in the toolbar after you complete the steps above. When you click this button, Safari displays the pop-up webpage from your web extension.

If you have trouble getting your extension to work, see [`Troubleshooting your Safari web extension`](troubleshooting-your-safari-web-extension.md).

##### Update Your Safari Web Extension in Ios

To deploy changes to your extension after installing it the first time, choose Product > Run. Xcode packages the most recent changes to your extension files in the iOS app. As soon as the build completes and Xcode installs the app on your device or selected simulator, your extension updates are ready to use in Safari.

##### Update Your Safari Web Extension in Macos

To deploy changes to your extension after installing it the first time, choose Product > Build. Xcode packages the most recent changes to your extension files in the macOS app. As soon as the build completes, your extension updates are ready to use in Safari.

## See Also

- [Distributing your Safari web extension](distributing-your-safari-web-extension.md)
  Get feedback on your extension from beta testers, then share your extension with customers in the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/running-your-safari-web-extension)*