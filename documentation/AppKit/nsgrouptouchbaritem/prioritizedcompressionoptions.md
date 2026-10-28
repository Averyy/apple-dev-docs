# prioritizedCompressionOptions

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The allowed compression options, in the order they should be applied.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var prioritizedCompressionOptions: [NSUserInterfaceCompressionOptions] { get set }
```

```objc
@property (copy) NSArray<NSUserInterfaceCompressionOptions *> * prioritizedCompressionOptions;
```

## Discussion

Use this property when you want to control the order of the system compression options, or if you want to use custom compression options.

The default value is an array containing all standard AppKit options, in the AppKit-defined order.

## See Also

### Configuring item compression
- [var effectiveCompressionOptions: NSUserInterfaceCompressionOptions](./effectivecompressionoptions.md)
  The compression options that are currently active on the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/prioritizedcompressionoptions)*