# fragmentsStatus

**Framework**: MediaExtension  
**Kind**: property

Indicates if the media asset contains fragments or is extendable by fragments.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var fragmentsStatus: MEFileInfo.FragmentsStatus { get set }
```

#### Discussion

The default value is [`MEFileInfo.FragmentsStatus.couldNotContainFragments`](mefileinfo/fragmentsstatus-swift.enum/couldnotcontainfragments.md).

## See Also

- [var duration: CMTime](mefileinfo/duration.md)
  The duration of the media asset, if available.
- [MEFileInfo.FragmentsStatus](mefileinfo/fragmentsstatus-swift.enum.md)
  An enumeration that describes if a media asset contains or supports fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mefileinfo/fragmentsstatus-swift.property)*