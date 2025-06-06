# init(nsUnderlineStyle:)

**Framework**: SwiftUI  
**Kind**: init

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

> **Note**: Use this initializer only if you need to convert an existing `NSUnderlineStyle` to a SwiftUI `Text.LineStyle`. Otherwise, create a `Text.LineStyle` using an initializer like [`init(pattern:color:)`](text/linestyle/init(pattern:color:).md).

Use this initializer only if you need to convert an existing `NSUnderlineStyle` to a SwiftUI `Text.LineStyle`. Otherwise, create a `Text.LineStyle` using an initializer like [`init(pattern:color:)`](text/linestyle/init(pattern:color:).md).

## Parameters

- `nsUnderlineStyle`: A value of    to wrap with  .

## See Also

- [init(pattern: Text.LineStyle.Pattern, color: Color?)](text/linestyle/init(pattern:color:).md)
  Creates a line style.
- [Text.LineStyle.Pattern](text/linestyle/pattern.md)
  The pattern, that the line has.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/linestyle/init(nsunderlinestyle:))*