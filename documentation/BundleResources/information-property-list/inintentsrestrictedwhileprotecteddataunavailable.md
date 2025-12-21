# INIntentsRestrictedWhileProtectedDataUnavailable

**Framework**: Bundle Resources  
**Kind**: typealias

The names of the intent classes your app can’t handle when the user locks the device or the system blocks access to protected data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- tvOS 14.0+
- visionOS 1.0+

#### Discussion

To specify this information in Xcode, add the intent class name to your app target’s Supported Intents in the Project Editor. Then set the Authentication level to Restricted While Locked or Protected Data Unavailable.

## See Also

- [INIntentsSupported](information-property-list/inintentssupported.md)
  The names of the intent classes your app handles directly.
- [INIntentsRestrictedWhileLocked](information-property-list/inintentsrestrictedwhilelocked.md)
  The names of the intent classes your app can’t handle when the user locks the device.
- [INSupportedMediaCategories](information-property-list/insupportedmediacategories.md)
  Types of media supported by your app’s media-playing intents.
- [NSFocusStatusUsageDescription](information-property-list/nsfocusstatususagedescription.md)
  A message that tells people why your app requests access to a person’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/inintentsrestrictedwhileprotecteddataunavailable)*