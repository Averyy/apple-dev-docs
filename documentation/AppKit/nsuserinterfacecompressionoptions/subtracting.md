# subtracting(_:)

**Framework**: AppKit  
**Kind**: method

Creates a new compression options object with the supplied options removed.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func subtracting(_ options: NSUserInterfaceCompressionOptions) -> NSUserInterfaceCompressionOptions
```

#### Return Value

A new `NSCompressibleUserInterfaceOptions` object with the supplied options removed.

## Parameters

- `options`: A set of compression options to remove from the current object.

## See Also

- [func union(NSUserInterfaceCompressionOptions) -> NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions/union(_:).md)
  Creates a new compression options object representing the union with the provided options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/subtracting(_:))*