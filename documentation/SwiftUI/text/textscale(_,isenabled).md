# textScale(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies a text scale to the text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func textScale(_ scale: Text.Scale, isEnabled: Bool = true) -> Text
```

## Return Value

Text with the specified scale applied.

## Parameters

- `scale`: The text scale to apply.
- `isEnabled`: If true the text scale is applied; otherwise text scale is unchanged.

## See Also

### Fitting text into available space
- [struct Scale](./scale.md)
  Defines text scales
- [Text.TruncationMode](./truncationmode.md)
  The type of truncation to apply to a line of text when it’s too long to fit in the available space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/textscale(_:isenabled:))*