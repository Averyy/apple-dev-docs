# init(nsUnderlineStyle:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a `Text.LineStyle` from `NSUnderlineStyle`.

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
init?(nsUnderlineStyle: NSUnderlineStyle)
```

#### Return Value

A new `Text.LineStyle` or `nil` when `nsUnderlineStyle` contains styles not supported by `Text.LineStyle`.

#### Discussion

> **Note**: Use this initializer only if you need to convert an existing `NSUnderlineStyle` to a SwiftUI `Text.LineStyle`. Otherwise, create a `Text.LineStyle` using an initializer like [`init(pattern:color:)`](./init%28pattern,color%29.md).

## Parameters

- `nsUnderlineStyle`: A value of `NSUnderlineStyle` to wrap with `Text.LineStyle`.

## See Also

### Creating a text line style
- [init(pattern: Text.LineStyle.Pattern, color: Color?)](./init%28pattern,color%29.md)
  Creates a line style.
- [Text.LineStyle.Pattern](./pattern.md)
  The pattern, that the line has.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/linestyle/init(nsunderlinestyle:))*