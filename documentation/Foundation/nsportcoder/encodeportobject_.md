# encodePortObject:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Encodes a given port so it can be properly reconstituted in the receiving process or thread.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (void) encodePortObject:(NSPort *) aport;
```

## Discussion

This method is primarily for use by `NSPort` objects themselves—you can always use the general `encode...Object:` methods to encode any object.

`NSPort` invokes this method in its [`encode(with:)`](../nscoding/encode%28with%29.md) method so that the appropriate kernel information for the port can be encoded. A subclass of `NSPortCoder` should not encode an `NSPort` by sending it an [`encode(with:)`](../nscoding/encode%28with%29.md) message. See [Subclassing NSCoder](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/subclassing.html#//apple_ref/doc/uid/20000951) for more information.

## Parameters

- `aport`: The port to encode.

## See Also

### Encoding NSPort Objects
- [- decodePortObject](./decodeportobject.md)
  Decodes and returns an `NSPort` object that was previously encoded with any of the general `encode...Object:` messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportcoder/encodeportobject:)*