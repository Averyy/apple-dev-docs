# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets state for the specified vertex attribute.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLVertexAttributeDescriptor *) attributeDesc atIndexedSubscript:(NSUInteger) index;
```

#### Discussion

If this method is called with `nil` for `attributeDesc` for any legal `index`, its vertex attribute state is set to the default values.

## Parameters

- `attributeDesc`: A descriptor that contains vertex attribute state.
- `index`: A specified index in the array of vertex attribute states.

## See Also

### Accessing a specified vertex attribute
- [subscript(Int) -> MTLVertexAttributeDescriptor!](./subscript%28_%29.md)
  Returns the state of the specified vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray/setobject:atindexedsubscript:)*