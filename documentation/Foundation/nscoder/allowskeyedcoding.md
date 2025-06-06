# allowsKeyedCoding

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the receiver supports keyed coding of objects.

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
var allowsKeyedCoding: Bool { get }
```

#### Discussion

[`false`](https://developer.apple.com/documentation/swift/false) by default. Concrete subclasses that support keyed coding, such as `NSKeyedArchiver`, need to override this property to return [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [Archives and Serializations Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
- [func containsValue(forKey: String) -> Bool](nscoder/containsvalue(forkey:).md)
  Returns a Boolean value that indicates whether an encoded value is available for a string.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](nscoder/decodingfailurepolicy-swift.property.md)
  The action the coder should take when decoding fails.
- [NSCoder.DecodingFailurePolicy](nscoder/decodingfailurepolicy-swift.enum.md)
  Policies describing the action the coder should take when encountering decode failures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/allowskeyedcoding)*