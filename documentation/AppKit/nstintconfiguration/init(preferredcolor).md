# init(preferredColor:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new tint configuration for the system to use when the app’s preferred accent color is in use.

**Availability**:
- macOS 11.0+

## Declaration

```swift
convenience init(preferredColor color: NSColor)
```

```objc
+ (instancetype) tintConfigurationWithPreferredColor:(NSColor *) color;
```

#### Discussion

Use this tint configuration for custom colors designed to match app-specific accent colors, but doesn’t look appropriate matched with a user-selected color. The tint configuation only uses the preferred color when the system accent color is `Multicolor`. If the system accent color is any other color, the tint configuration defers to the accent color.

## Parameters

- `color`: The color used when the system accent color is `Multicolor`.

## See Also

### Initializing a Tint Configuration
- [convenience init(fixedColor: NSColor)](./init%28fixedcolor%29.md)
  Creates a new tint configuration using a specific color value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration/init(preferredcolor:))*