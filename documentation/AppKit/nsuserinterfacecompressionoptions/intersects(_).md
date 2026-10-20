# intersects(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the supplied compression options intersect with the current instance’s options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func intersects(_ options: NSUserInterfaceCompressionOptions) -> Bool
```

```objc
- (BOOL) intersectsOptions:(NSUserInterfaceCompressionOptions *) options;
```

#### Return Value

Returns [`true`](../../Swift/true.md) if at least one of the supplied options is present in the instance’s options, or [`false`](../../Swift/false.md) otherwise.

## Parameters

- `options`: A compression options object to compare with the current instance.

## See Also

### Comparing compression options
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that denotes whether the option is empty.
- [func contains(NSUserInterfaceCompressionOptions) -> Bool](./contains%28_%29.md)
  Determines whether the supplied compression options are all present in the current instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/intersects(_:))*