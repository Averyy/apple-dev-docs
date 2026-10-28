# duration

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The duration of the media asset, if available.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var duration: CMTime { get set }
```

```objc
@property (nonatomic) CMTime duration;
```

## Discussion

This value is [`invalid`](../../CoreMedia/cmtime/invalid.md) if the duration isn’t available.

## See Also

### Inspecting file properties
- [var fragmentsStatus: MEFileInfo.FragmentsStatus](./fragmentsstatus-swift.property.md)
  Indicates if the media asset contains fragments or is extendable by fragments.
- [MEFileInfo.FragmentsStatus](./fragmentsstatus-swift.enum.md)
  An enumeration that describes if a media asset contains or supports fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mefileinfo/duration)*