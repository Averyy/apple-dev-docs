# kColorSyncProfileCacheSeed

**Framework**: ColorSync  
**Kind**: var

The current profile-cache seed (uint32_t), sent with [`kColorSyncProfileRepositoryChangeNotification`](kcolorsyncprofilerepositorychangenotification.md).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var kColorSyncProfileCacheSeed: Unmanaged<CFString>!
```

## See Also

- [var kColorSyncProfileRepositoryChangeNotification: Unmanaged<CFString>!](kcolorsyncprofilerepositorychangenotification.md)
  A notification that ColorSync posts when the profile repository changes.
- [var kColorSyncWaitForCacheReply: Unmanaged<CFString>!](kcolorsyncwaitforcachereply.md)
  An iteration option that waits for the profile cache to finish updating before returning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncprofilecacheseed)*