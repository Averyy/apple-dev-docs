# supportAttributeStrides

**Framework**: Metal  
**Kind**: property

Controls whether Metal should reserve memory for attribute strides in the argument table.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var supportAttributeStrides: Bool { get set }
```

#### Discussion

Set this value to true if you intend to provide dynamic attribute strides when binding vertex array buffers to the argument table by calling [`setAddress(_:attributeStride:index:)`](mtl4argumenttable/setaddress(_:attributestride:index:).md)

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttabledescriptor/supportattributestrides)*