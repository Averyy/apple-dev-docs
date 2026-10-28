# setObjectZone:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the memory zone used to allocate decoded objects.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (void) setObjectZone:(NSZone *) zone;
```

## Discussion

If `zone` is `nil`, or if this method is never invoked, the default zone is used, as given by `NSDefaultMallocZone()`.

## Parameters

- `zone`: The memory zone used to allocate decoded objects.

## See Also

### Managing an NSUnarchiver
- [var isAtEnd: Bool](./isatend.md)
  A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding.
- [- objectZone](./objectzone-c.method.md)
  Returns the memory zone used to allocate decoded objects.
- [var systemVersion: UInt32](./systemversion-swift.property.md)
  The system version number in effect when the archive was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/setobjectzone:)*