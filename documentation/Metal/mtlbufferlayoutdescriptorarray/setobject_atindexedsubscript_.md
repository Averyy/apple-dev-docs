# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets the state of the specified buffer layout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLBufferLayoutDescriptor *) bufferDesc atIndexedSubscript:(NSUInteger) index;
```

## Parameters

- `bufferDesc`: A descriptor that contains buffer layout state.
- `index`: An index in the array of buffer layouts.

## See Also

### Array accessors
- [subscript(Int) -> MTLBufferLayoutDescriptor!](./subscript%28_%29.md)
  Returns the state of the specified buffer layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptorarray/setobject:atindexedsubscript:)*