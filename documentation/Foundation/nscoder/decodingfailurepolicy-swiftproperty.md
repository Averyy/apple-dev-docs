# decodingFailurePolicy

**Framework**: Foundation  
**Kind**: property

The action the coder should take when decoding fails.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var decodingFailurePolicy: NSCoder.DecodingFailurePolicy { get }
```

#### Discussion

A decode call can fail for the following reasons:

- The keyed archive data is corrupt or missing.
- A type mismatch occurs, such as expecting a class by calling [`decodeObject(of:forKey:)`](nscoder/decodeobject(of:forkey:)-7tmft.md) but encountering a numeric type instead. This also occurs when [`decodeInteger(forKey:)`](nscoder/decodeinteger(forkey:).md) encounters a value encoded as floating-point, or vice versa.
- A secure coding violation occurs. This happens when you attempt to decode an object that doesn’t conform to [`NSSecureCoding`](nssecurecoding.md). This also happens when the encoded type doesn’t match any of the types passed to [`decodeObject(of:forKey:)`](nscoder/decodeobject(of:forkey:)-roif.md).

## See Also

- [var allowsKeyedCoding: Bool](nscoder/allowskeyedcoding.md)
  A Boolean value that indicates whether the receiver supports keyed coding of objects.
- [func containsValue(forKey: String) -> Bool](nscoder/containsvalue(forkey:).md)
  Returns a Boolean value that indicates whether an encoded value is available for a string.
- [NSCoder.DecodingFailurePolicy](nscoder/decodingfailurepolicy-swift.enum.md)
  Policies describing the action the coder should take when encountering decode failures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy-swift.property)*