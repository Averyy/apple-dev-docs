# prioritizedCompressionOptions

**Framework**: AppKit  
**Kind**: property

The allowed compression options, in the order they should be applied.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@MainActor
var prioritizedCompressionOptions: [NSUserInterfaceCompressionOptions] { get set }
```

#### Discussion

Use this property when you want to control the order of the system compression options, or if you want to use custom compression options.

The default value is an array containing all standard AppKit options, in the AppKit-defined order.

## See Also

- [var effectiveCompressionOptions: NSUserInterfaceCompressionOptions](nsgrouptouchbaritem/effectivecompressionoptions.md)
  The compression options that are currently active on the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/prioritizedcompressionoptions)*