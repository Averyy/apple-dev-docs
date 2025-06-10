# insertNewLine(configuration:from:to:startMarker:endMarker:)

**Framework**: PaperKit  
**Kind**: method

Add a line element on top of the paper.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
mutating func insertNewLine(configuration: ShapeConfiguration, from start: CGPoint, to end: CGPoint, startMarker lineStartMarker: Bool = false, endMarker lineEndMarker: Bool = false)
```

## Parameters

- `configuration`: The configuration of the line to insert.
- `start`: The start position of the line.
- `end`: The end position of the line.
- `lineStartMarker`: True if the start of the line has a marker / arrow.
- `lineEndMarker`: True if the end of the line has a marker / arrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup/insertnewline(configuration:from:to:startmarker:endmarker:))*