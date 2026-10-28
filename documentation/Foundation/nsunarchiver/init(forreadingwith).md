# init(forReadingWith:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSUnarchiver` object initialized to read an archive from a given data object.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedUnarchiver instead

## Declaration

```swift
init?(forReadingWith data: Data)
```

```objc
- (instancetype) initForReadingWithData:(NSData *) data;
```

## Return Value

An `NSUnarchiver` object initialized to read an archive from `data`. Returns `nil` if `data` is not a valid archive.

## Discussion

The method decodes the system version number that was archived in `data` prepares the `NSUnarchiver` object for a subsequent invocation of [`decodeObject()`](../nscoder/decodeobject%28%29.md).

Raises an `NSInvalidArgumentException` if `data` is `nil`.

## Parameters

- `data`: The archive data.

## See Also

### Related Documentation
- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
- [var systemVersion: UInt32](./systemversion-swift.property.md)
  The system version number in effect when the archive was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/init(forreadingwith:))*