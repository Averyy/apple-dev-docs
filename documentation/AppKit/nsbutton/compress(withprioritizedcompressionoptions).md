# compress(withPrioritizedCompressionOptions:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the priority compression options for this button.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func compress(withPrioritizedCompressionOptions prioritizedOptions: [NSUserInterfaceCompressionOptions])
```

```objc
- (void) compressWithPrioritizedCompressionOptions:(NSArray<NSUserInterfaceCompressionOptions *> *) prioritizedOptions;
```

## Parameters

- `prioritizedOptions`: An array of interface compression options.

## See Also

### Managing button compression
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](./activecompressionoptions.md)
  The compression options active for this button.
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](./minimumsize%28withprioritizedcompressionoptions%29.md)
  Returns the minimum size of the button by using the compression options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/compress(withprioritizedcompressionoptions:))*