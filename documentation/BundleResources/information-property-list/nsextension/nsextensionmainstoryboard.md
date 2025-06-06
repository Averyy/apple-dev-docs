# NSExtensionMainStoryboard

**Framework**: Bundle Resources  
**Kind**: typealias

The name of the app extension’s main storyboard file.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- visionOS 1.0+

#### Discussion

This key is mutually exclusive with [`NSExtensionPrincipalClass`](information-property-list/nsextension/nsextensionprincipalclass.md). Typically, Xcode sets the value of this key when creating an App Extension target in your project. If you change the name of your storyboard file, remember to update the value of this key.

> ❗ **Important**:  If the app extension’s `Info.plist` file contains both keys, the system won’t load the extension.

 If the app extension’s `Info.plist` file contains both keys, the system won’t load the extension.

## See Also

- [NSExtensionActionWantsFullScreenPresentation](information-property-list/nsextension/nsextensionactionwantsfullscreenpresentation.md)
  A Boolean value indicating whether the Action extension is presented in full screen.
- [NSExtensionOverridesHostUIAppearance](information-property-list/nsextension/nsextensionoverrideshostuiappearance.md)
  A Boolean value indicating whether the app extension ignores appearance changes made by the host app.
- [NSExtensionPointIdentifier](information-property-list/nsextension/nsextensionpointidentifier.md)
  The extension point that supports an app extension.
- [NSExtensionPrincipalClass](information-property-list/nsextension/nsextensionprincipalclass.md)
  The custom class that implements an app extension’s primary view or functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionmainstoryboard)*