# attributeNamed(_:)

**Framework**: Model I/O  
**Kind**: method

Returns the vertex attribute with the specified name in the vertex descriptor.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func attributeNamed(_ name: String) -> MDLVertexAttribute?
```

#### Return Value

The descriptor’s vertex attribute with the specified name, or `nil` if the [`attributes`](mdlvertexdescriptor/attributes.md) array does not contain a vertex attribute with that name.

## Parameters

- `name`: The attribute name for which to retrieve data. See Vertex Attributes for standard attribute names.

## See Also

- [var attributes: NSMutableArray](mdlvertexdescriptor/attributes.md)
  The list of vertex attributes described by the vertex descriptor.
- [func addOrReplaceAttribute(MDLVertexAttribute)](mdlvertexdescriptor/addorreplaceattribute(_:).md)
  Adds the specified vertex attribute to the vertex descriptor, replacing any existing attribute with the same name.
- [func setPackedOffsets()](mdlvertexdescriptor/setpackedoffsets.md)
  Sets the offset for each vertex attribute to the minimum value to pack vertex data together in a single buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor/attributenamed(_:))*