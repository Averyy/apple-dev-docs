# boundingBox

**Framework**: AppKit  
**Kind**: property

The rectangle that bounds the image representation.

**Availability**:
- macOS ?+

## Declaration

```swift
var boundingBox: NSRect { get }
```

#### Discussion

The rectangle bounding the receiver. This rectangle is obtained from the the `picFrame` field in the picture header. See the Carbon QuickDraw Manager documentation for information on the picture header

## See Also

- [var pictRepresentation: Data](nspictimagerep/pictrepresentation.md)
  The image representation’s PICT data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspictimagerep/boundingbox)*