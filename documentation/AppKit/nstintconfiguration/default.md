# default

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The system tints the content using the system default value for its context.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class var `default`: NSTintConfiguration { get }
```

```objc
@property (class, strong, readonly) NSTintConfiguration * defaultTintConfiguration;
```

## See Also

### Setting the Tint Color
- [class var monochrome: NSTintConfiguration](./monochrome.md)
  The content always displays in monochrome.
- [var baseTintColor: NSColor?](./basetintcolor.md)
  The color the system supplies when you create a tint configuration.
- [var equivalentContentTintColor: NSColor?](./equivalentcontenttintcolor.md)
  A color object that matches the effective content tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration/default)*