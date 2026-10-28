# NSWorkspace.IconCreationOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that describe options for creating icons.

**Availability**:
- macOS

## Declaration

```swift
struct IconCreationOptions
```

```c
enum NSWorkspaceIconCreationOptions : NSUInteger;
```

## Overview

Use these constants with the [`setIcon(_:forFile:options:)`](./seticon%28_,forfile,options%29.md) method. You can combine these using the C bitwise OR operator.

## Topics

### Creation Options
- [static var excludeQuickDrawElementsIconCreationOption: NSWorkspace.IconCreationOptions](./iconcreationoptions/excludequickdrawelementsiconcreationoption.md)
  An option to suppress generation of the QuickDraw format icon representations that are used in macOS 10.0 through macOS 10.4.
- [static var exclude10_4ElementsIconCreationOption: NSWorkspace.IconCreationOptions](./iconcreationoptions/exclude10_4elementsiconcreationoption.md)
  An option to suppress generation of the new higher resolution icon representations that are supported in macOS 10.4.
### Initializers
- [init(rawValue: UInt)](./iconcreationoptions/init%28rawvalue%29.md)
  Initializes an icon creation option using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing Icons
- [func icon(forFile: String) -> NSImage](./icon%28forfile%29.md)
  Returns an image containing the icon for the specified file.
- [func icon(forFiles: [String]) -> NSImage?](./icon%28forfiles%29.md)
  Returns an image containing the icon for the specified files.
- [func icon(for: UTType) -> NSImage](./icon%28for%29.md)
  Returns an image containing the icon for the specified content type.
- [func setIcon(NSImage?, forFile: String, options: NSWorkspace.IconCreationOptions) -> Bool](./seticon%28_,forfile,options%29.md)
  Sets the icon for the file or directory at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/iconcreationoptions)*