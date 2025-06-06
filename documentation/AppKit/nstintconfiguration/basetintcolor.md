# baseTintColor

**Framework**: AppKit  
**Kind**: property

The color the system supplies when you create a tint configuration.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var baseTintColor: NSColor? { get }
```

#### Discussion

This property is `nil` if the tint configuration wasn’t created using an [`NSColor`](nscolor.md) object.

## See Also

- [class var `default`: NSTintConfiguration](nstintconfiguration/default.md)
  The system tints the content using the system default value for its context.
- [class var monochrome: NSTintConfiguration](nstintconfiguration/monochrome.md)
  The content always displays in monochrome.
- [var equivalentContentTintColor: NSColor?](nstintconfiguration/equivalentcontenttintcolor.md)
  A color object that matches the effective content tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration/basetintcolor)*