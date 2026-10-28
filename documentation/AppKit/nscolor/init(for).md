# init(for:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns the color object specified by the given control tint.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: NSControlTint does not describe the full range of available control accent colors. Use +[NSColor controlAccentColor] instead.

## Declaration

```swift
init(for controlTint: NSControlTint)
```

```objc
+ (NSColor *) colorForControlTint:(NSControlTint) controlTint;
```

## Return Value

The `NSColor` object.

## Parameters

- `controlTint`: The control tint for which to return a color object. This is one of the tint settings.

## See Also

### Related Documentation
- [class var currentControlTint: NSControlTint](./currentcontroltint.md)
  The current system control tint color.
### Creating a system tint color
- [enum NSControlTint](../nscontroltint.md)
  Constants for specifying a cell’s tint color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(for:))*