# length

**Framework**: Foundation  
**Kind**: property

The number of UTF-16 code units in the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var length: Int { get }
```

#### Discussion

This number includes the individual characters of composed character sequences, so you cannot use this property to determine if a string will be visible when printed or how long it will appear.

## See Also

- [func size(withAttributes: [NSAttributedString.Key : Any]?) -> CGSize](nsstring/size(withattributes:).md)
  Returns the bounding box size the receiver occupies when drawn with the given attributes.
- [func lengthOfBytes(using: UInt) -> Int](nsstring/lengthofbytes(using:).md)
  Returns the number of bytes required to store the receiver in a given encoding.
- [func maximumLengthOfBytes(using: UInt) -> Int](nsstring/maximumlengthofbytes(using:).md)
  Returns the maximum number of bytes needed to store the receiver in a given encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/length)*