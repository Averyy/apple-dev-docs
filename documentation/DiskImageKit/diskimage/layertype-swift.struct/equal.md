# ==(_:_:)

**Framework**: DiskImageKit  
**Kind**: op

Equatable implementation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static func == (lhs: DiskImage.LayerType, rhs: DiskImage.LayerType) -> Bool
```

#### Discussion

Two LayerType values are equal if they represent the same layer type. For overlay layers, the blockCount parameter is ignored in the comparison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/layertype-swift.struct/==(_:_:))*