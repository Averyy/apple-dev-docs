# activeCompressionOptions

**Framework**: AppKit  
**Kind**: property

The compression options active for this button.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@NSCopying
@MainActor var activeCompressionOptions: NSUserInterfaceCompressionOptions { get }
```

#### Discussion

Only compression options that have been applied and are actively being respected are returned. For more information about managing button sizes when space is restriced, see [`NSUserInterfaceCompressionOptions`](nsuserinterfacecompressionoptions.md).

## See Also

- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](nsbutton/compress(withprioritizedcompressionoptions:).md)
  Sets the priority compression options for this button.
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](nsbutton/minimumsize(withprioritizedcompressionoptions:).md)
  Returns the minimum size of the button by using the compression options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/activecompressionoptions)*