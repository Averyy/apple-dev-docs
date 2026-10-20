# init(fixedColor:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new tint configuration using a specific color value.

**Availability**:
- macOS 11.0+

## Declaration

```swift
convenience init(fixedColor color: NSColor)
```

```objc
+ (instancetype) tintConfigurationWithFixedColor:(NSColor *) color;
```

## Parameters

- `color`: The color used regardless of the system accent color.

## See Also

### Initializing a Tint Configuration
- [convenience init(preferredColor: NSColor)](./init%28preferredcolor%29.md)
  Creates a new tint configuration for the system to use when the app’s preferred accent color is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration/init(fixedcolor:))*