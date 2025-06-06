# debugDescription

**Framework**: Swift  
**Kind**: property

A textual representation of the value, suitable for debugging.

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
var debugDescription: String { get }
```

#### Discussion

This property has the same value as the `description` property, except that NaN values are printed in an extended format.

## See Also

- [func hash(into: inout Hasher)](float/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var description: String](float/description.md)
  A textual representation of the value.
- [var customMirror: Mirror](float/custommirror.md)
  A mirror that reflects the `Float` instance.
- [var hashValue: Int](float/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/debugdescription)*