# Supporting Previous Versions of iOS

**Framework**: CarPlay

Make your CarPlay-enabled apps compatible with older system versions, such as iOS 13 and earlier.

#### Overview

In iOS 14 and later, CarPlay adds more app categories and further entitlements to support them. The framework also provides new templates that you can use to build your app’s user interface.

Some of the new app categories supersede existing ones, such as audio and communication. Using the proper combination of frameworks and entitlements, you can ensure that your app is compatible with iOS 13 and earlier, and iOS 14 and later. To learn about requesting entitlements for your CarPlay-enabled app, see [`Requesting CarPlay Entitlements`](requesting-carplay-entitlements.md).

##### Add Backward Compatibility to Audio Apps

In iOS 14 and later, the CarPlay framework includes templates that you can use to build your audio app’s user interface. To use these templates, include the `com.apple.developer.carplay-audio` entitlement.

Before iOS 14, you built CarPlay-enabled audio apps using the Media Player framework, and included the `com.apple.developer.playable-content` entitlement. To support iOS 13 and earlier, use the [`Media Player`](https://developer.apple.com/documentation/MediaPlayer) framework and this entitlement. Your app will also work in iOS 14 and later.

Audio apps can use the CarPlay framework, the Media Player framework, or both. Include the applicable entitlements that match the frameworks you’re using. To be compatible with iOS 13 and earlier, as well as iOS 14 and later, specify keys for both entitlements in the entitlements file.

```plist
<key>com.apple.developer.playable-content</key>
<true/>
<key>com.apple.developer.carplay-audio</key>
<true/>
```

##### Add Backward Compatibility to Communication Apps

In iOS 14 and later, the CarPlay framework includes templates that you can use to build your communication app’s user interface. To use these templates, include the `com.apple.developer.carplay-communication` entitlement.

Your communication app can use the CarPlay, [`SiriKit`](https://developer.apple.com/documentation/SiriKit), or [`CallKit`](https://developer.apple.com/documentation/CallKit) framework, or a combination of the three. Include the entitlements that match the frameworks you’re using. If you use the CarPlay framework, your app can’t present a custom user interface in iOS 13 or earlier. However, users can still interact with your app as they have in previous versions.

The following example shows what you might add to a messaging app’s entitlements file, providing compatibility with iOS 13 and earlier, as well as iOS 14 and later:

```plist
<key>com.apple.developer.carplay-communication</key>
<true/>
<key>com.apple.developer.carplay-messaging</key>
<true/>
```

If your CarPlay-enabled communication app includes VoIP features, provide support for doc://com.apple.documentation/documentation/sirikit/instartcallintent. If the VoIP app targets iOS 14 or earlier, provide support for doc://com.apple.documentation/documentation/sirikit/instartaudiocallintent and doc://com.apple.documentation/documentation/sirikit/insearchcallhistoryintent in addition to doc://com.apple.documentation/documentation/sirikit/instartcallintent.

## See Also

- [Requesting CarPlay Entitlements](requesting-carplay-entitlements.md)
  Configure your CarPlay-enabled app with the entitlements it requires.
- [Displaying Content in CarPlay](displaying-content-in-carplay.md)
  Use scenes to present your app’s content on the vehicle’s built-in screen.
- [Using the CarPlay Simulator](using-the-carplay-simulator.md)
  Configure Simulator to run and debug your CarPlay-enabled app.
- [class CPTemplateApplicationScene](cptemplateapplicationscene.md)
  A CarPlay scene that controls your app’s user interface.
- [protocol CPTemplateApplicationSceneDelegate](cptemplateapplicationscenedelegate.md)
  The methods for responding to the life cycle events of your app’s scene.
- [class CPSessionConfiguration](cpsessionconfiguration.md)
  An object that provides vehicle properties and configuration for the CarPlay environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/supporting-previous-versions-of-ios)*