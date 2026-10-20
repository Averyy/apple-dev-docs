# contains(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the supplied compression options are all present in the current instance.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func contains(_ options: NSUserInterfaceCompressionOptions) -> Bool
```

```objc
- (BOOL) containsOptions:(NSUserInterfaceCompressionOptions *) options;
```

#### Return Value

Returns [`true`](../../Swift/true.md) if all the supplied options are present in the instance’s options, or [`false`](../../Swift/false.md) otherwise.

## Parameters

- `options`: A compression options object to compare with the current instance.

## See Also

### Comparing compression options
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that denotes whether the option is empty.
- [func intersects(NSUserInterfaceCompressionOptions) -> Bool](./intersects%28_%29.md)
  Determines whether the supplied compression options intersect with the current instance’s options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/contains(_:))*