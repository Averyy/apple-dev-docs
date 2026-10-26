# isAtEnd

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedUnarchiver instead

## Declaration

```swift
var isAtEnd: Bool { get }
```

```objc
@property (readonly, getter=isAtEnd) BOOL atEnd;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver has reached the end of the encoded data while decoding, otherwise [`false`](../../Swift/false.md).

You can invoke this method after invoking `decodeObject` to discover whether the archive contains extra data following the encoded object graph. If it does, you can either ignore this anomaly or consider it an error.

## See Also

### Managing an NSUnarchiver
- [var systemVersion: UInt32](./systemversion-swift.property.md)
  The system version number in effect when the archive was created.
- [- objectZone](./objectzone-c.method.md)
  Returns the memory zone used to allocate decoded objects.
- [- setObjectZone:](./setobjectzone_.md)
  Sets the memory zone used to allocate decoded objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/isatend)*