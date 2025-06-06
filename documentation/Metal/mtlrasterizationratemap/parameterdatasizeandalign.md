# parameterDataSizeAndAlign

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The size and alignment requirements to contain the coordinate transformation information in this rate map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var parameterDataSizeAndAlign: MTLSizeAndAlign { get }
```

## Mentions

- [Scaling Variable Rasterization Rate Content](scaling-variable-rasterization-rate-content.md)

#### Discussion

To convert coordinate values inside your shader, pass the rate map data into the shader in a [`MTLBuffer`](mtlbuffer.md) object. The place in the buffer where you store the parameter information must have at least the size and alignment provided by this property.

## See Also

- [func copyParameterData(buffer: any MTLBuffer, offset: Int)](mtlrasterizationratemap/copyparameterdata(buffer:offset:).md)
  Copies the parameter data into the provided buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemap/parameterdatasizeandalign)*