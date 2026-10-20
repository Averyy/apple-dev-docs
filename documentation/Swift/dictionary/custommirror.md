# customMirror

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

A mirror that reflects the dictionary.

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
var customMirror: Mirror { get }
```

Available when `Key` conforms to `Hashable`.

## See Also

### Describing a Dictionary
- [var description: String](./description.md)
  A string that represents the contents of the dictionary.
- [var debugDescription: String](./debugdescription.md)
  A string that represents the contents of the dictionary, suitable for debugging.
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/custommirror)*