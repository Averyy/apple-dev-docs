# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets state for the specified attribute.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLAttributeDescriptor *) attributeDesc atIndexedSubscript:(NSUInteger) index;
```

## Parameters

- `attributeDesc`: A descriptor that contains attribute state.
- `index`: A specified index in the array of vertex attribute states.

## See Also

### Accessing attribute state objects
- [subscript(Int) -> MTLAttributeDescriptor!](./subscript%28_%29.md)
  Returns the state of the specified attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattributedescriptorarray/setobject:atindexedsubscript:)*