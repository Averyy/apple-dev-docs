# offset

**Framework**: Metal  
**Kind**: property

The offset, in bytes, from the start of the buffer that contains the attribute data to the start of the data itself.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var offset: Int { get set }
```

#### Discussion

Check the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

- [var bufferIndex: Int](mtlattributedescriptor/bufferindex.md)
  The index in the buffer argument table for the buffer that contains the data for this attribute.
- [var format: MTLAttributeFormat](mtlattributedescriptor/format.md)
  The format of the attribute’s data.
- [enum MTLAttributeFormat](mtlattributeformat.md)
  The data format options for acceleration structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattributedescriptor/offset)*