# init(forWritingWith:)

**Framework**: Foundation  
**Kind**: init

Returns an archiver, initialized to encode stream and version information into a given mutable data object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
init(forWritingWith mdata: NSMutableData)
```

#### Return Value

An archiver object, initialized to encode stream and version information into `data`.

#### Discussion

Raises an `NSInvalidArgumentException` if `data` is `nil`.

## Parameters

- `mdata`: The mutable data object into which to write the archive. This value must not be  .

## See Also

- [var archiverData: NSMutableData](nsarchiver/archiverdata.md)
  The receiver’s archive data.
- [Archives and Serializations Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/init(forwritingwith:))*