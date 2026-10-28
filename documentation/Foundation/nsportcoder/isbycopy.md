# isBycopy

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the receiver is encoding an object by copying it.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (BOOL) isBycopy;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver is encoding an object by copying it, [`false`](../../Swift/false.md) if it expects a proxy.

## Discussion

See [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i) for more information.

## See Also

### Checking for Encoding
- [- isByref](./isbyref.md)
  Returns a Boolean value that indicates whether the receiver is encoding an object by reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportcoder/isbycopy)*