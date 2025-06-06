# subscript(_:)

**Framework**: Metal  
**Kind**: subscript

Returns the pipeline buffer descriptor at the specified array index.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
subscript(bufferIndex: Int) -> MTLPipelineBufferDescriptor! { get set }
```

#### Return Value

The descriptor for the buffer bound at this index.

## Parameters

- `bufferIndex`: The array index of the requested pipeline buffer descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelinebufferdescriptorarray/subscript(_:))*