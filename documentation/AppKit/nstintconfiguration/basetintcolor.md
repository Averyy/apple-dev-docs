# baseTintColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color the system supplies when you create a tint configuration.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var baseTintColor: NSColor? { get }
```

```objc
@property (strong, readonly, nullable) NSColor * baseTintColor;
```

#### Discussion

This property is `nil` if the tint configuration wasn’t created using an [`NSColor`](../nscolor.md) object.

## See Also

### Setting the Tint Color
- [class var `default`: NSTintConfiguration](./default.md)
  The system tints the content using the system default value for its context.
- [class var monochrome: NSTintConfiguration](./monochrome.md)
  The content always displays in monochrome.
- [var equivalentContentTintColor: NSColor?](./equivalentcontenttintcolor.md)
  A color object that matches the effective content tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration/basetintcolor)*