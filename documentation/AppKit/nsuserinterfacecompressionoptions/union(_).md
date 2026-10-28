# union(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new compression options object representing the union with the provided options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func union(_ options: NSUserInterfaceCompressionOptions) -> NSUserInterfaceCompressionOptions
```

```objc
- (NSUserInterfaceCompressionOptions *) optionsByAddingOptions:(NSUserInterfaceCompressionOptions *) options;
```

## Return Value

A new `NSCompressibleUserInterfaceOptions` object which represents the union with the supplied compression options.

## Parameters

- `options`: A set of compression options to add to the current object.

## See Also

### Combining compression options
- [func subtracting(NSUserInterfaceCompressionOptions) -> NSUserInterfaceCompressionOptions](./subtracting%28_%29.md)
  Creates a new compression options object with the supplied options removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/union(_:))*