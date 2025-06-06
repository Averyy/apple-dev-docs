# Distributing your Safari web extension

**Framework**: Safari Services

Get feedback on your extension from beta testers, then share your extension with customers in the App Store.

#### Overview

Safari supports distributing a web extension in a macOS app, a visionOS app, an iOS app, or a Mac app created using Mac Catalyst.

You can test your unsigned macOS web extension in Safari during development and beta testing, but you need to sign your extension and containing macOS app to securely distribute it to users in the App Store.

You can test your unsigned visionOS or iOS web extension in the simulators during development. For testing on device, beta testing with other users, and distributing to users in the App Store, you need to sign your extension and containing visionOS or iOS app.

##### Join the Apple Developer Program

To distribute your web extension, first join the Apple Developer Program. The Apple Developer Program provides resources to securely distribute your extension in the App Store. To learn more about enrolling in the program, see [`Apple Developer Program`](https://developer.apple.comhttps://developer.apple.com/programs/).

##### Distribute Your Extension for Beta Testing in Visionos or Ios

For beta testing in visionOS or iOS, you can send beta testers a signed, ad-hoc distribution copy of the app containing your extension, and then instruct them how to install it. For more information, see [`Distributing your app to registered devices`](https://developer.apple.com/documentation/Xcode/distributing-your-app-to-registered-devices).

Alternatively, you can distribute your extension to a wider group of beta testers using TestFlight. For more information, see [`Distributing your app for beta testing and releases`](https://developer.apple.com/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases).

##### Distribute Your Extension for Beta Testing in Macos

Safari only supports signed extensions, but for beta testing, you can send beta testers an unsigned copy of the macOS app containing your extension, and then instruct them how to enable testing. For more information on creating and uploading an archive, see [`Distributing your app for beta testing and releases`](https://developer.apple.com/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases). Use the “Copy App” distribution method, which will distribute a macOS app without code signing, to create a beta version of your macOS app and web extension.

Then, instruct your beta testers to enable unsigned extensions in Safari or the Mac web app in order to test your extension. For more information, see [`Configure Safari in macOS to run unsigned extensions`](running-your-safari-web-extension#Configure-Safari-in-macOS-to-run-unsigned-extensions.md).

##### Distribute Your Extension in the App Store

When you’re ready to ship your extension in the App Store, gather the assets and details you need to create your product page. For more information, see [`Making the Most of the App Store`](https://developer.apple.comhttps://developer.apple.com/app-store/).

If you provide your extension on more than one platform, consider selling them together as one product to improve the purchasing experience for your users. For more information, see [`Offering Universal Purchase`](https://developer.apple.comhttps://developer.apple.com/support/universal-purchase/).

Create an archive of your app to use for submission, then upload the archive to the App Store. For more information, see [`Distributing your app for beta testing and releases`](https://developer.apple.com/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases). Choose the “App Store Connect” distribution method to send your macOS or iOS app binary to the app store in preparation for publishing.

Submit your app for review and publishing. For more information, see the section titled “Publish on the App Store” in [`Distributing your app for beta testing and releases`](https://developer.apple.com/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases).

##### Distribute Your Developer Id Signed and Notarized Extension Outside the Mac App Store

If you provide your extension in macOS and don’t want to use the Mac App Store for distribution, you can sign and notarize your extension’s app with a Developer ID to distribute it outside the Mac App Store. For more information, see [`Developer ID`](https://developer.apple.comhttps://developer.apple.com/support/developer-id/) and [`Notarizing macOS software before distribution`](https://developer.apple.com/documentation/Security/notarizing-macos-software-before-distribution).

## See Also

- [Running your Safari web extension](running-your-safari-web-extension.md)
  Install and update your extension in Safari as you make changes in development.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/distributing-your-safari-web-extension)*