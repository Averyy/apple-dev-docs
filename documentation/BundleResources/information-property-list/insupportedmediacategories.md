# INSupportedMediaCategories

**Framework**: Bundle Resources  
**Kind**: typealias

Types of media supported by your app’s media-playing intents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- tvOS 14.0+
- visionOS 1.0+

#### Discussion

Specify one or more media categories to allow Siri to invoke your app’s intent handling when a user asks to play media. Use `INMediaCategoryGeneral` for media that doesn’t fit into any of the other categories, like white noise or sound effects.

To specify this information in Xcode, add [`INPlayMediaIntent`](https://developer.apple.com/documentation/Intents/INPlayMediaIntent) to your app’s list of Supported Intents. Then select the relevant media types in the list that appears.

## See Also

- [INIntentsSupported](information-property-list/inintentssupported.md)
  The names of the intent classes your app handles directly.
- [INIntentsRestrictedWhileLocked](information-property-list/inintentsrestrictedwhilelocked.md)
  The names of the intent classes your app can’t handle when the user locks the device.
- [INIntentsRestrictedWhileProtectedDataUnavailable](information-property-list/inintentsrestrictedwhileprotecteddataunavailable.md)
  The names of the intent classes your app can’t handle when the user locks the device or the system blocks access to protected data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/insupportedmediacategories)*