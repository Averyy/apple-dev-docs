# minimumSize(withPrioritizedCompressionOptions:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the minimum size a view can achieve by applying the supplied compression options.

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

The minimum size of a view when applying the supplied compression options.

## Discussion

Compression options that are handled by the system are not included in the supplied array.

## Parameters

- `prioritizedOptions`: An array of compression options that the view should apply to reduce its size.

## See Also

### Querying Compression Status
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](./activecompressionoptions.md)
  The compression options that are currently applied to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompression/minimumsize(withprioritizedcompressionoptions:))*