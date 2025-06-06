# isAtEnd

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
var isAtEnd: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver has reached the end of the encoded data while decoding, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

You can invoke this method after invoking `decodeObject` to discover whether the archive contains extra data following the encoded object graph. If it does, you can either ignore this anomaly or consider it an error.

## See Also

- [var systemVersion: UInt32](nsunarchiver/systemversion-swift.property.md)
  The system version number in effect when the archive was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/isatend)*