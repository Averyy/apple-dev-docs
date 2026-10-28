# debugDescription

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

This property has the same value as the `description` property, except that NaN values are printed in an extended format.

## See Also

### Describing a Double
- [var description: String](./description.md)
  A textual representation of the value.
- [var customMirror: Mirror](./custommirror.md)
  A mirror that reflects the `Double` instance.
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/debugdescription)*