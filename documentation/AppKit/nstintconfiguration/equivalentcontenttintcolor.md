# equivalentContentTintColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A color object that matches the effective content tint.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var equivalentContentTintColor: NSColor? { get }
```

```objc
@property (strong, readonly, nullable) NSColor * equivalentContentTintColor;
```

## Discussion

The value of this property is an [`NSColor`](../nscolor.md) that matches the represented content tint. This property is `nil` if the system can’t represent the content tint as an [`NSColor`](../nscolor.md).

## See Also

### Setting the Tint Color
- [class var `default`: NSTintConfiguration](./default.md)
  The system tints the content using the system default value for its context.
- [class var monochrome: NSTintConfiguration](./monochrome.md)
  The content always displays in monochrome.
- [var baseTintColor: NSColor?](./basetintcolor.md)
  The color the system supplies when you create a tint configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration/equivalentcontenttintcolor)*