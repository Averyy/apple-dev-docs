# NSWorkspace.IconCreationOptions

**Framework**: AppKit  
**Kind**: struct

Constants that describe options for creating icons.

**Availability**:
- macOS ?+

## Declaration

```swift
struct IconCreationOptions
```

#### Overview

Use these constants with the [`setIcon(_:forFile:options:)`](nsworkspace/seticon(_:forfile:options:).md) method. You can combine these using the C bitwise OR operator.

## Topics

### Creation Options
- [static var excludeQuickDrawElementsIconCreationOption: NSWorkspace.IconCreationOptions](nsworkspace/iconcreationoptions/excludequickdrawelementsiconcreationoption.md)
  An option to suppress generation of the QuickDraw format icon representations that are used in macOS 10.0 through macOS 10.4.
- [static var exclude10_4ElementsIconCreationOption: NSWorkspace.IconCreationOptions](nsworkspace/iconcreationoptions/exclude10_4elementsiconcreationoption.md)
  An option to suppress generation of the new higher resolution icon representations that are supported in macOS 10.4.
### Initializers
- [init(rawValue: UInt)](nsworkspace/iconcreationoptions/init(rawvalue:).md)
  Initializes an icon creation option using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func icon(forFile: String) -> NSImage](nsworkspace/icon(forfile:).md)
  Returns an image containing the icon for the specified file.
- [func icon(forFiles: [String]) -> NSImage?](nsworkspace/icon(forfiles:).md)
  Returns an image containing the icon for the specified files.
- [func icon(for: UTType) -> NSImage](nsworkspace/icon(for:).md)
  Returns an image containing the icon for the specified content type.
- [func setIcon(NSImage?, forFile: String, options: NSWorkspace.IconCreationOptions) -> Bool](nsworkspace/seticon(_:forfile:options:).md)
  Sets the icon for the file or directory at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/iconcreationoptions)*