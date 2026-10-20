# debugDescription

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

A string that represents the contents of the set, suitable for debugging.

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

Available when `Element` conforms to `Hashable`.

## See Also

### Describing a Set
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var description: String](./description.md)
  A string that represents the contents of the set.
- [var customMirror: Mirror](./custommirror.md)
  A mirror that reflects the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/debugdescription)*