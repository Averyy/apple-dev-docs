# activeCompressionOptions

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The compression options active for this button.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@NSCopying
var activeCompressionOptions: NSUserInterfaceCompressionOptions { get }
```

```objc
@property (copy, readonly) NSUserInterfaceCompressionOptions * activeCompressionOptions;
```

#### Discussion

Only compression options that have been applied and are actively being respected are returned. For more information about managing button sizes when space is restriced, see [`NSUserInterfaceCompressionOptions`](../nsuserinterfacecompressionoptions.md).

## See Also

### Managing button compression
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](./compress%28withprioritizedcompressionoptions%29.md)
  Sets the priority compression options for this button.
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](./minimumsize%28withprioritizedcompressionoptions%29.md)
  Returns the minimum size of the button by using the compression options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/activecompressionoptions)*