# minimumSize(withPrioritizedCompressionOptions:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the minimum size of the button by using the compression options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func minimumSize(withPrioritizedCompressionOptions prioritizedOptions: [NSUserInterfaceCompressionOptions]) -> NSSize
```

```objc
- (NSSize) minimumSizeWithPrioritizedCompressionOptions:(NSArray<NSUserInterfaceCompressionOptions *> *) prioritizedOptions;
```

## Return Value

The size of the compressed button.

## Parameters

- `prioritizedOptions`: An array of interface compression options.

## See Also

### Managing button compression
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](./activecompressionoptions.md)
  The compression options active for this button.
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](./compress%28withprioritizedcompressionoptions%29.md)
  Sets the priority compression options for this button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/minimumsize(withprioritizedcompressionoptions:))*