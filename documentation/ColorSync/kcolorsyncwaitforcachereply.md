# kColorSyncWaitForCacheReply

**Framework**: ColorSync  
**Kind**: var

An iteration option that waits for the profile cache to finish updating before returning.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncWaitForCacheReply: Unmanaged<CFString>!
```

## See Also

- [var kColorSyncProfileRepositoryChangeNotification: Unmanaged<CFString>!](kcolorsyncprofilerepositorychangenotification.md)
  A notification that ColorSync posts when the profile repository changes.
- [var kColorSyncProfileCacheSeed: Unmanaged<CFString>!](kcolorsyncprofilecacheseed.md)
  The current profile-cache seed (uint32_t), sent with [`kColorSyncProfileRepositoryChangeNotification`](kcolorsyncprofilerepositorychangenotification.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncwaitforcachereply)*