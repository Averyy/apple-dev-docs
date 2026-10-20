# activeCompressionOptions

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The compression options that are currently applied to the view.

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

This property includes only those compression options applied to the view that are actively being respected.

## See Also

### Querying Compression Status
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](./minimumsize%28withprioritizedcompressionoptions%29.md)
  Returns the minimum size a view can achieve by applying the supplied compression options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompression/activecompressionoptions)*