# init(forWritingWith:)

**Framework**: Foundation  
**Kind**: init

Initializes an archiver to encode data into a given a mutable-data object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(forWritingWith data: NSMutableData)
```

#### Discussion

When you finish encoding data, you must invoke [`finishEncoding()`](nskeyedarchiver/finishencoding().md) at which point `data` is filled. The format of the receiver is `NSPropertyListBinaryFormat_v1_0`.

## Parameters

- `data`: The mutable-data object into which the archive is written.

## See Also

- [Archives and Serializations Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
- [init(requiringSecureCoding: Bool)](nskeyedarchiver/init(requiringsecurecoding:).md)
  Creates an archiver to encode data, and optionally disables secure coding.
- [init()](nskeyedarchiver/init.md)
  Initializes an archiver to encode data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/init(forwritingwith:))*