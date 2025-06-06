# minimumSize(withPrioritizedCompressionOptions:)

**Framework**: AppKit  
**Kind**: method

Returns the minimum size of the button by using the compression options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@MainActor
func minimumSize(withPrioritizedCompressionOptions prioritizedOptions: [NSUserInterfaceCompressionOptions]) -> NSSize
```

#### Return Value

The size of the compressed button.

## Parameters

- `prioritizedOptions`: An array of interface compression options.

## See Also

- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](nsbutton/activecompressionoptions.md)
  The compression options active for this button.
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](nsbutton/compress(withprioritizedcompressionoptions:).md)
  Sets the priority compression options for this button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/minimumsize(withprioritizedcompressionoptions:))*