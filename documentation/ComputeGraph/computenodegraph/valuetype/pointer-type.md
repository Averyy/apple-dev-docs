# ComputeNodeGraph.ValueType.pointer(type:)

**Framework**: ComputeGraph  
**Kind**: case

Value is a `strided_buffer<element>`, a flexible method for referencing buffer data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
case pointer(type: ComputeNodeGraph.PointerDefinition)
```

#### Discussion

The type is set at compile time, and you configure the buffer’s address, stride, and count at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/valuetype/pointer(type:))*