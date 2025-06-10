# supportAttributeStrides

**Framework**: Metal  
**Kind**: property

Controls whether Metal should reserve memory for attribute strides in the argument table.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var supportAttributeStrides: Bool { get set }
```

#### Discussion

Set this value to true if you intend to provide dynamic attribute strides when binding vertex array buffers to the argument table by calling [`setAddress(_:attributeStride:index:)`](mtl4argumenttable/setaddress(_:attributestride:index:).md)

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttabledescriptor/supportattributestrides)*