# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets the state of the specified vertex buffer layout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLVertexBufferLayoutDescriptor *) bufferDesc atIndexedSubscript:(NSUInteger) index;
```

#### Discussion

If this method is called with `nil` for `bufferDesc` for any legal index, the [`MTLVertexBufferLayoutDescriptor`](../mtlvertexbufferlayoutdescriptor.md) object in the array is set to the default values.

## Parameters

- `bufferDesc`: A descriptor that contains vertex buffer layout state.
- `index`: An index in the array of vertex buffer layouts.

## See Also

### Accessing a specified vertex buffer layout
- [subscript(Int) -> MTLVertexBufferLayoutDescriptor!](./subscript%28_%29.md)
  Returns the state of the specified vertex buffer layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray/setobject:atindexedsubscript:)*