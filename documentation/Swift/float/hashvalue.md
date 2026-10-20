# hashValue

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The hash value.

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
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

### Describing a Float
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var description: String](./description.md)
  A textual representation of the value.
- [var debugDescription: String](./debugdescription.md)
  A textual representation of the value, suitable for debugging.
- [var customMirror: Mirror](./custommirror.md)
  A mirror that reflects the `Float` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/hashvalue)*