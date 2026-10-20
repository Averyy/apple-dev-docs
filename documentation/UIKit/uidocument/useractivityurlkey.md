# userActivityURLKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

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

```c
extern NSString * const NSUserActivityDocumentURLKey;
```

#### Discussion

You use this key in the [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary of an [`NSUserActivity`](../../Foundation/nsuseractivity.md) object. Its value is the URL of the document associated with the user activity.

When the `NSUbiquitousDocumentUserActivityType` key is present in a [`CFBundleDocumentTypes`](../../BundleResources/information-property-list/cfbundledocumenttypes.md) entry, AppKit automatically creates an [`NSUserActivity`](../../Foundation/nsuseractivity.md) object for documents in iCloud, using the given activity type.

## See Also

### Constants
- [UIDocument.ChangeKind](./changekind.md)
  Constants that specify the kind of change to a document.
- [UIDocument.SaveOperation](./saveoperation.md)
  Constants that specify the type of save operation.
- [UIDocument.State](./state.md)
  Constants that specify the document state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/useractivityurlkey)*