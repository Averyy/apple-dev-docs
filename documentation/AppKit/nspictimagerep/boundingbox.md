# boundingBox

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rectangle that bounds the image representation.

**Availability**:
- macOS

## Declaration

```swift
var boundingBox: NSRect { get }
```

```objc
@property (readonly) NSRect boundingBox;
```

#### Discussion

The rectangle bounding the receiver. This rectangle is obtained from the the `picFrame` field in the picture header. See the Carbon QuickDraw Manager documentation for information on the picture header

## See Also

### Getting Data
- [var pictRepresentation: Data](./pictrepresentation.md)
  The image representation’s PICT data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspictimagerep/boundingbox)*