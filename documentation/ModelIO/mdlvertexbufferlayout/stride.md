# stride

**Framework**: Model I/O  
**Kind**: property

The stride, in bytes, between data for separate vertices in a vertex buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var stride: Int { get set }
```

#### Discussion

For example, if a vertex buffer contains interleaved data for two attributes, the stride is typically the sum of data sizes for those two attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexbufferlayout/stride)*