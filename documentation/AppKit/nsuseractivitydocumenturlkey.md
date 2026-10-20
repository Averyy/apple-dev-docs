# NSUserActivityDocumentURLKey

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The key that identifies the document associated with a user activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
let NSUserActivityDocumentURLKey: String
```

```c
extern NSString * const NSUserActivityDocumentURLKey;
```

#### Discussion

You use this key in the [`userInfo`](../Foundation/nsuseractivity/userinfo.md) dictionary of an [`NSUserActivity`](../Foundation/nsuseractivity.md) object. Its value is the URL of the document associated with the user activity.

When the `NSUbiquitousDocumentUserActivityType` key is present in a [`CFBundleDocumentTypes`](../BundleResources/information-property-list/cfbundledocumenttypes.md) entry, AppKit automatically creates an [`NSUserActivity`](../Foundation/nsuseractivity.md) object for documents in iCloud, using the given activity type.

## See Also

### Supporting User Activities
- [var userActivity: NSUserActivity?](./nsdocument/useractivity.md)
  An object that encapsulates a user activity the document supports.
- [func updateUserActivityState(NSUserActivity)](./nsdocument/updateuseractivitystate%28_%29.md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuseractivitydocumenturlkey)*