# NSUserInterfaceCompression

**Framework**: AppKit  
**Kind**: protocol

A protocol that describes how a UI control should redisplay when space is restricted.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSUserInterfaceCompression
```

#### Overview

A control that adopts this protocol has the ability to resize itself when space is at a premium.

## Topics

### Compressing the UI
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](nsuserinterfacecompression/compress(withprioritizedcompressionoptions:).md)
  Compress the view by applying the specified compression options.
### Querying Compression Status
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](nsuserinterfacecompression/minimumsize(withprioritizedcompressionoptions:).md)
  Returns the minimum size a view can achieve by applying the supplied compression options.
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](nsuserinterfacecompression/activecompressionoptions.md)
  The compression options that are currently applied to the view.

## Relationships

### Conforming Types
- [NSButton](nsbutton.md)
- [NSPopUpButton](nspopupbutton.md)
- [NSSegmentedControl](nssegmentedcontrol.md)
- [NSStatusBarButton](nsstatusbarbutton.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompression)*