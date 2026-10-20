# standardOptions

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An option that represents the union of all standard compression options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@NSCopying
class var standardOptions: NSUserInterfaceCompressionOptions { get }
```

```objc
@property (class, copy, readonly) NSUserInterfaceCompressionOptions * standardOptions;
```

## See Also

### Creating standard options
- [class var hideImages: NSUserInterfaceCompressionOptions](./hideimages.md)
  An option specifying that views should hide their images.
- [class var hideText: NSUserInterfaceCompressionOptions](./hidetext.md)
  An option specifying that views should hide their text.
- [class var reduceMetrics: NSUserInterfaceCompressionOptions](./reducemetrics.md)
  An option specifying that views should reduce their internal metrics.
- [class var breakEqualWidths: NSUserInterfaceCompressionOptions](./breakequalwidths.md)
  An option specifying that views should no longer maintain equal width constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/standardoptions)*