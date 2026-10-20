# init(pattern:color:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a line style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(pattern: Text.LineStyle.Pattern = .solid, color: Color? = nil)
```

## Parameters

- `pattern`: The pattern of the line.
- `color`: The color of the line. If not provided, the foreground color of text is used.

## See Also

### Creating a text line style
- [init?(nsUnderlineStyle: NSUnderlineStyle)](./init%28nsunderlinestyle%29.md)
  Creates a `Text.LineStyle` from `NSUnderlineStyle`.
- [Text.LineStyle.Pattern](./pattern.md)
  The pattern, that the line has.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/linestyle/init(pattern:color:))*