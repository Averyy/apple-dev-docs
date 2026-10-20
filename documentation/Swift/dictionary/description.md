# description

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

A string that represents the contents of the dictionary.

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

Available when `Key` conforms to `Hashable`.

## See Also

### Describing a Dictionary
- [var debugDescription: String](./debugdescription.md)
  A string that represents the contents of the dictionary, suitable for debugging.
- [var customMirror: Mirror](./custommirror.md)
  A mirror that reflects the dictionary.
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/description)*