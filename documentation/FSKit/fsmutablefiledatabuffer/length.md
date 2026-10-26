# length

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The data length of the buffer.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var length: Int { get }
```

```objc
@property (readonly) NSUInteger length;
```

## See Also

### Accessing buffer properties
- [func withUnsafeMutableBytes<R, E>((UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R](./withunsafemutablebytes%28_%29.md)
  Performs the given closure with an unsafe pointer to the underlying bytes of the data buffer.
- [- mutableBytes](./mutablebytes.md)
  The byte data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmutablefiledatabuffer/length)*