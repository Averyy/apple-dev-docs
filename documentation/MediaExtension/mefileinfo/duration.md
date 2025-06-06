# duration

**Framework**: MediaExtension  
**Kind**: property

The duration of the media asset, if available.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var duration: CMTime { get set }
```

#### Discussion

This value is [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid) if the duration isn’t available.

## See Also

- [var fragmentsStatus: MEFileInfo.FragmentsStatus](mefileinfo/fragmentsstatus-swift.property.md)
  Indicates if the media asset contains fragments or is extendable by fragments.
- [MEFileInfo.FragmentsStatus](mefileinfo/fragmentsstatus-swift.enum.md)
  An enumeration that describes if a media asset contains or supports fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mefileinfo/duration)*