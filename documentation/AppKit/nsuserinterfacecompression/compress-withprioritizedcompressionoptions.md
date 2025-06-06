# compress(withPrioritizedCompressionOptions:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Compress the view by applying the specified compression options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func compress(withPrioritizedCompressionOptions prioritizedOptions: [NSUserInterfaceCompressionOptions])
```

#### Discussion

When the system calls this method, the view should resize itself according to the compression options supplied.

Compression options that are handled by the system are not included in the supplied array.

## Parameters

- `prioritizedOptions`: An array of compression options that the view should apply to reduce its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompression/compress(withprioritizedcompressionoptions:))*