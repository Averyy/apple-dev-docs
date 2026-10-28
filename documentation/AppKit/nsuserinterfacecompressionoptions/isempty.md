# isEmpty

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that denotes whether the option is empty.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var isEmpty: Bool { get }
```

```objc
@property (readonly, getter=isEmpty) BOOL empty;
```

## Discussion

Returns [`true`](../../Swift/true.md) if the option is equivalent to the empty set, or [`false`](../../Swift/false.md) otherwise.

## See Also

### Comparing compression options
- [func contains(NSUserInterfaceCompressionOptions) -> Bool](./contains%28_%29.md)
  Determines whether the supplied compression options are all present in the current instance.
- [func intersects(NSUserInterfaceCompressionOptions) -> Bool](./intersects%28_%29.md)
  Determines whether the supplied compression options intersect with the current instance’s options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/isempty)*