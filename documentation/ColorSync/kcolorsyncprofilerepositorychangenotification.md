# kColorSyncProfileRepositoryChangeNotification

**Framework**: ColorSync  
**Kind**: var

A notification that ColorSync posts when the profile repository changes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncProfileRepositoryChangeNotification: Unmanaged<CFString>!
```

## See Also

- [var kColorSyncProfileCacheSeed: Unmanaged<CFString>!](kcolorsyncprofilecacheseed.md)
  The current profile-cache seed (uint32_t), sent with [`kColorSyncProfileRepositoryChangeNotification`](kcolorsyncprofilerepositorychangenotification.md).
- [var kColorSyncWaitForCacheReply: Unmanaged<CFString>!](kcolorsyncwaitforcachereply.md)
  An iteration option that waits for the profile cache to finish updating before returning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncprofilerepositorychangenotification)*