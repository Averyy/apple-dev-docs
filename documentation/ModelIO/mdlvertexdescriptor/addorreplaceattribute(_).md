# addOrReplaceAttribute(_:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Adds the specified vertex attribute to the vertex descriptor, replacing any existing attribute with the same name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addOrReplaceAttribute(_ attribute: MDLVertexAttribute)
```

```objc
- (void) addOrReplaceAttribute:(MDLVertexAttribute *) attribute;
```

## Discussion

If the vertex descriptor contains an attribute whose [`name`](../mdlvertexattribute/name.md) property is the same as that of the `attribute` parameter, the new attribute replaces the existing attribute in the [`attributes`](./attributes.md) array. Otherwise, this method adds the new attribute to the end of the [`attributes`](./attributes.md) array.

## Parameters

- `attribute`: The vertex attribute to add to the vertex descriptor.

## See Also

### Working with Vertex Attributes
- [var attributes: NSMutableArray](./attributes.md)
  The list of vertex attributes described by the vertex descriptor.
- [func attributeNamed(String) -> MDLVertexAttribute?](./attributenamed%28_%29.md)
  Returns the vertex attribute with the specified name in the vertex descriptor.
- [func setPackedOffsets()](./setpackedoffsets%28%29.md)
  Sets the offset for each vertex attribute to the minimum value to pack vertex data together in a single buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor/addorreplaceattribute(_:))*