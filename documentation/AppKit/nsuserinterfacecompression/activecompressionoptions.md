# activeCompressionOptions

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The compression options that are currently applied to the view.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@NSCopying
var activeCompressionOptions: NSUserInterfaceCompressionOptions { get }
```

#### Discussion

This property includes only those compression options applied to the view that are actively being respected.

## See Also

- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](nsuserinterfacecompression/minimumsize(withprioritizedcompressionoptions:).md)
  Returns the minimum size a view can achieve by applying the supplied compression options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompression/activecompressionoptions)*