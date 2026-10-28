# init(forWritingWith:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an archiver to encode data into a given a mutable-data object.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 5.0

> **Deprecated**: Use [`init(requiringSecureCoding:)`](./init%28requiringsecurecoding%29.md) instead.

## Declaration

```swift
init(forWritingWith data: NSMutableData)
```

```objc
- (instancetype) initForWritingWithMutableData:(NSMutableData *) data;
```

## Discussion

When you finish encoding data, you must invoke [`finishEncoding()`](./finishencoding%28%29.md) at which point `data` is filled. The format of the receiver is `NSPropertyListBinaryFormat_v1_0`.

## Parameters

- `data`: The mutable-data object into which the archive is written.

## See Also

### Related Documentation
- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
### Creating a Keyed Archiver
- [init(requiringSecureCoding: Bool)](./init%28requiringsecurecoding%29.md)
  Creates an archiver to encode data, and optionally disables secure coding.
- [init()](./init%28%29.md)
  Initializes an archiver to encode data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/init(forwritingwith:))*