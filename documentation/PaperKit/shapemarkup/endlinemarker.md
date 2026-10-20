# endLineMarker

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The line marker used at the end of an open shape path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var endLineMarker: ShapeMarkup.LineMarker { get set }
```

#### Discussion

Line markers are only visible on open paths. Use `shape.supportsLineMarkers` to check whether the current shape supports line markers. Closed shapes like `.rectangle` and `.ellipse` ignore this property.

Default is `.none`.

## See Also

### Configuring line markers
- [var startLineMarker: ShapeMarkup.LineMarker](./startlinemarker.md)
  The line marker used at the start of an open shape path.
- [ShapeMarkup.LineMarker](./linemarker.md)
  A marker that can be attached to a line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/endlinemarker)*