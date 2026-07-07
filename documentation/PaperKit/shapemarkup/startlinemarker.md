# startLineMarker

**Framework**: PaperKit  
**Kind**: property

The line marker used at the start of an open shape path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var startLineMarker: ShapeMarkup.LineMarker { get set }
```

#### Discussion

Line markers are only visible on open paths. Use `shape.supportsLineMarkers` to check whether the current shape supports line markers. Closed shapes like `.rectangle` and `.ellipse` ignore this property.

Default is `.none`.

## See Also

- [var endLineMarker: ShapeMarkup.LineMarker](shapemarkup/endlinemarker.md)
  The line marker used at the end of an open shape path.
- [ShapeMarkup.LineMarker](shapemarkup/linemarker.md)
  A marker that can be attached to a line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/startlinemarker)*