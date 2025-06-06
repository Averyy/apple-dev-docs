# underline(_:pattern:color:)

**Framework**: RealityKit  
**Kind**: method

Applies an underline to the text in this view.

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
func underline(_ isActive: Bool = true, pattern: Text.LineStyle.Pattern = .solid, color: Color? = nil) -> some View
```

#### Return Value

A view where text has a line running along its baseline.

## Parameters

- `isActive`: A Boolean value that indicates whether underline   is added. The default value is  .
- `pattern`: The pattern of the line. The default value is  .
- `color`: The color of the underline. If   is  , the   underline uses the default foreground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/underline(_:pattern:color:))*