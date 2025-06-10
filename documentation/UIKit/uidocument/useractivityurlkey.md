# userActivityURLKey

**Framework**: UIKit  
**Kind**: property

The key that identifies the document associated with a user activity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class let userActivityURLKey: String
```

#### Discussion

You use this key in the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSUserActivity/userInfo) dictionary of an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object. Its value is the URL of the document associated with the user activity.

When the `NSUbiquitousDocumentUserActivityType` key is present in a [`CFBundleDocumentTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes) entry, AppKit automatically creates an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object for documents in iCloud, using the given activity type.

## See Also

- [UIDocument.ChangeKind](uidocument/changekind.md)
  Constants that specify the kind of change to a document.
- [UIDocument.SaveOperation](uidocument/saveoperation.md)
  Constants that specify the type of save operation.
- [UIDocument.State](uidocument/state.md)
  Constants that specify the document state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/useractivityurlkey)*