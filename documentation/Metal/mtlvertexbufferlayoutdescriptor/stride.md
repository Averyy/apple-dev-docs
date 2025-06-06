# stride

**Framework**: Metal  
**Kind**: property

The number of bytes between the first byte of two consecutive vertices in a buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var stride: Int { get set }
```

#### Discussion

Check the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions for `stride`.

## See Also

- [var stepFunction: MTLVertexStepFunction](mtlvertexbufferlayoutdescriptor/stepfunction.md)
  The circumstances under which the vertex and its attributes are presented to the vertex function.
- [var stepRate: Int](mtlvertexbufferlayoutdescriptor/steprate.md)
  The interval at which the vertex and its attributes are presented to the vertex function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor/stride)*