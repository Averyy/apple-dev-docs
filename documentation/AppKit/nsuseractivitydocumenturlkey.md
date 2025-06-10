# NSUserActivityDocumentURLKey

**Framework**: AppKit  
**Kind**: var

The key that identifies the document associated with a user activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
let NSUserActivityDocumentURLKey: String
```

#### Discussion

You use this key in the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSUserActivity/userInfo) dictionary of an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object. Its value is the URL of the document associated with the user activity.

When the `NSUbiquitousDocumentUserActivityType` key is present in a [`CFBundleDocumentTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes) entry, AppKit automatically creates an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object for documents in iCloud, using the given activity type.

## See Also

- [var userActivity: NSUserActivity?](nsdocument/useractivity.md)
  An object that encapsulates a user activity the document supports.
- [func updateUserActivityState(NSUserActivity)](nsdocument/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuseractivitydocumenturlkey)*