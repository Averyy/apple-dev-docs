# breakEqualWidths

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An option specifying that views should no longer maintain equal width constraints.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@NSCopying
class var breakEqualWidths: NSUserInterfaceCompressionOptions { get }
```

```objc
@property (class, copy, readonly) NSUserInterfaceCompressionOptions * breakEqualWidthsOption;
```

## Discussion

This option is handled by the system, and no action is required by the views.

## See Also

### Creating standard options
- [class var hideImages: NSUserInterfaceCompressionOptions](./hideimages.md)
  An option specifying that views should hide their images.
- [class var hideText: NSUserInterfaceCompressionOptions](./hidetext.md)
  An option specifying that views should hide their text.
- [class var reduceMetrics: NSUserInterfaceCompressionOptions](./reducemetrics.md)
  An option specifying that views should reduce their internal metrics.
- [class var standardOptions: NSUserInterfaceCompressionOptions](./standardoptions.md)
  An option that represents the union of all standard compression options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/breakequalwidths)*