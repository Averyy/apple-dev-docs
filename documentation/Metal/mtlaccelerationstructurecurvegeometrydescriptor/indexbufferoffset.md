# indexBufferOffset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The offset, in bytes, to the index data in the buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var indexBufferOffset: Int { get set }
```

```objc
@property (nonatomic) NSUInteger indexBufferOffset;
```

## Discussion

The offset needs to be a multiple of the index data type you configure with the [`indexType`](./indextype.md) property. You also need to align the offset to both the index type’s size and the platform’s buffer alignment requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/indexbufferoffset)*