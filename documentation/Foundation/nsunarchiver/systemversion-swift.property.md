# systemVersion

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The system version number in effect when the archive was created.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedUnarchiver instead

## Declaration

```swift
var systemVersion: UInt32 { get }
```

```objc
@property (readonly) unsigned int systemVersion;
```

## Discussion

This information is available as soon as the receiver has been initialized.

## See Also

### Managing an NSUnarchiver
- [var isAtEnd: Bool](./isatend.md)
  A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding.
- [- objectZone](./objectzone-c.method.md)
  Returns the memory zone used to allocate decoded objects.
- [- setObjectZone:](./setobjectzone_.md)
  Sets the memory zone used to allocate decoded objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/systemversion-swift.property)*