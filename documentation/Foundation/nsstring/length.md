# length

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSUInteger length;
```

#### Discussion

This number includes the individual characters of composed character sequences, so you cannot use this property to determine if a string will be visible when printed or how long it will appear.

## See Also

### Related Documentation
- [func size(withAttributes: [NSAttributedString.Key : Any]?) -> CGSize](./size%28withattributes%29.md)
  Returns the bounding box size the receiver occupies when drawn with the given attributes.
### Getting a String’s Length
- [func lengthOfBytes(using: UInt) -> Int](./lengthofbytes%28using%29.md)
  Returns the number of bytes required to store the receiver in a given encoding.
- [func maximumLengthOfBytes(using: UInt) -> Int](./maximumlengthofbytes%28using%29.md)
  Returns the maximum number of bytes needed to store the receiver in a given encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/length)*