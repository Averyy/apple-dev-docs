# hash(into:)

**Framework**: Swift  
**Kind**: method

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

## Parameters

- `hasher`: The hasher to use when combining the components   of this instance.

## See Also

- [var description: String](string/description.md)
  The value of this string.
- [var debugDescription: String](string/debugdescription.md)
  A representation of the string that is suitable for debugging.
- [var customMirror: Mirror](string/custommirror.md)
  A mirror that reflects the `String` instance.
- [var hashValue: Int](string/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/hash(into:))*