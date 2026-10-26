# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets a pipeline buffer descriptor at the specified array index.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLPipelineBufferDescriptor *) buffer atIndexedSubscript:(NSUInteger) bufferIndex;
```

## Parameters

- `buffer`: The pipeline buffer descriptor to set in the array.
- `bufferIndex`: The array index in which to set the given pipeline buffer descriptor.

## See Also

### Accessing array elements
- [subscript(Int) -> MTLPipelineBufferDescriptor!](./subscript%28_%29.md)
  Returns the pipeline buffer descriptor at the specified array index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelinebufferdescriptorarray/setobject:atindexedsubscript:)*