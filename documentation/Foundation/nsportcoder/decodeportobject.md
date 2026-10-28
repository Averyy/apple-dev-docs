# decodePortObject

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes and returns an `NSPort` object that was previously encoded with any of the general `encode...Object:` messages.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (NSPort *) decodePortObject;
```

## Return Value

An `NSPort` object that was previously encoded with any of the general `encode...Object:` messages.

## Discussion

This method is primarily for use by `NSPort` objects themselves—you can always use [`decodeObject()`](../nscoder/decodeobject%28%29.md) to decode any object.

`NSPort` invokes this method in its [`init(coder:)`](../nscoding/init%28coder%29.md) method so the appropriate kernel information for the port can be decoded. A subclass of `NSPortCoder` shouldn’t decode an `NSPort` by sending it an [`init(coder:)`](../nscoding/init%28coder%29.md) message. See [Subclassing NSCoder](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/subclassing.html#//apple_ref/doc/uid/20000951) for more information.

## See Also

### Encoding NSPort Objects
- [- encodePortObject:](./encodeportobject_.md)
  Encodes a given port so it can be properly reconstituted in the receiving process or thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportcoder/decodeportobject)*