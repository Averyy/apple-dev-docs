# strikethrough(_:pattern:color:)

**Framework**: App Intents  
**Kind**: method

Applies a strikethrough to the text in this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func strikethrough(_ isActive: Bool = true, pattern: Text.LineStyle.Pattern = .solid, color: Color? = nil) -> some View
```

#### Return Value

A view where text has a line through its center.

## Parameters

- `isActive`: A Boolean value that indicates whether   strikethrough is added. The default value is  .
- `pattern`: The pattern of the line. The default value is  .
- `color`: The color of the strikethrough. If   is  , the   strikethrough uses the default foreground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/strikethrough(_:pattern:color:))*