# monochrome

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The content always displays in monochrome.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class var monochrome: NSTintConfiguration { get }
```

```objc
@property (class, strong, readonly) NSTintConfiguration * monochromeTintConfiguration;
```

## Discussion

Content marked as monochrome remains monochrome regardless of the system accent color.

## See Also

### Setting the Tint Color
- [class var `default`: NSTintConfiguration](./default.md)
  The system tints the content using the system default value for its context.
- [var baseTintColor: NSColor?](./basetintcolor.md)
  The color the system supplies when you create a tint configuration.
- [var equivalentContentTintColor: NSColor?](./equivalentcontenttintcolor.md)
  A color object that matches the effective content tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstintconfiguration/monochrome)*