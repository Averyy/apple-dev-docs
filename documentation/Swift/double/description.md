# description

**Framework**: Swift  
**Kind**: property

A textual representation of the value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var description: String { get }
```

#### Discussion

For any finite value, this property provides a string that can be converted back to an instance of `Double` without rounding errors.  That is, if `x` is an instance of `Double`, then `Double(x.description) == x` is always true.  For any NaN value, the property’s value is “nan”, and for positive and negative infinity its value is “inf” and “-inf”.

## See Also

- [var debugDescription: String](double/debugdescription.md)
  A textual representation of the value, suitable for debugging.
- [var customMirror: Mirror](double/custommirror.md)
  A mirror that reflects the `Double` instance.
- [func hash(into: inout Hasher)](double/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/description)*