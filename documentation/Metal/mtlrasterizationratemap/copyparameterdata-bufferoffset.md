# copyParameterData(buffer:offset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Copies the parameter data into the provided buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func copyParameterData(buffer: any MTLBuffer, offset: Int)
```

#### Discussion

To convert coordinate values inside your shader, pass the rate map data into the shader in a [`MTLBuffer`](mtlbuffer.md) object. Use the [`parameterDataSizeAndAlign`](mtlrasterizationratemap/parameterdatasizeandalign.md) property to determine the size and alignment requirements for the buffer.

## Parameters

- `buffer`: The buffer object to copy the data into. It must have a   storage mode, and there must be enough room in the buffer to store the data.
- `offset`: The location in the buffer to copy the data to. The offset must be a multiple of the parameter alignment.

## See Also

- [var parameterDataSizeAndAlign: MTLSizeAndAlign](mtlrasterizationratemap/parameterdatasizeandalign.md)
  The size and alignment requirements to contain the coordinate transformation information in this rate map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemap/copyparameterdata(buffer:offset:))*