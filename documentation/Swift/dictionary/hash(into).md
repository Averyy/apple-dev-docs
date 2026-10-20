# hash(into:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Hashes the essential components of this value by feeding them into the given hasher.

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
func hash(into hasher: inout Hasher)
```

Available when `Key` conforms to `Hashable` and `Value` conforms to `Hashable`.

## Parameters

- `hasher`: The hasher to use when combining the components of this instance.

## See Also

### Describing a Dictionary
- [var description: String](./description.md)
  A string that represents the contents of the dictionary.
- [var debugDescription: String](./debugdescription.md)
  A string that represents the contents of the dictionary, suitable for debugging.
- [var customMirror: Mirror](./custommirror.md)
  A mirror that reflects the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/hash(into:))*