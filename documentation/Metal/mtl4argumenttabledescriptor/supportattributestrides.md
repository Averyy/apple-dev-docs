# supportAttributeStrides

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite) BOOL supportAttributeStrides;
```

## Discussion

Set this value to true if you intend to provide dynamic attribute strides when binding vertex array buffers to the argument table by calling [`setAddress(_:attributeStride:index:)`](../mtl4argumenttable/setaddress%28_,attributestride,index%29.md)

The default value of this property is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttabledescriptor/supportattributestrides)*