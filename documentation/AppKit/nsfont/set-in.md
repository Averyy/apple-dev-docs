# set(in:)

**Framework**: AppKit  
**Kind**: method

Sets this font as the font for the specified graphics context.

**Availability**:
- macOS ?+

## Declaration

```swift
func set(in graphicsContext: NSGraphicsContext)
```

#### Discussion

This method sets the font for the graphics system but does not affect the higher-level settings of the Cocoa text system, which are controlled by text attributes.

## Parameters

- `graphicsContext`: The graphics context for which the font is set.

## See Also

- [func set()](nsfont/set.md)
  Sets this font as the font for the current graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/set(in:))*