# init(preferredColor:)

**Framework**: AppKit  
**Kind**: init

Creates a new tint configuration for the system to use when the app’s preferred accent color is in use.

**Availability**:
- macOS 11.0+

## Declaration

```swift
convenience init(preferredColor color: NSColor)
```

#### Discussion

Use this tint configuration for custom colors designed to match app-specific accent colors, but doesn’t look appropriate matched with a user-selected color. The tint configuation only uses the preferred color when the system accent color is `Multicolor`. If the system accent color is any other color, the tint configuration defers to the accent color.

## Parameters

- `color`: The color used when the system accent color is  .

## See Also

- [convenience init(fixedColor: NSColor)](nstintconfiguration/init(fixedcolor:).md)
  Creates a new tint configuration using a specific color value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration/init(preferredcolor:))*