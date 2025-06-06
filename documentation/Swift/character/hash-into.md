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

- [var description: String](character/description.md)
  A textual representation of this instance.
- [var debugDescription: String](character/debugdescription.md)
  A textual representation of the character, suitable for debugging.
- [var customMirror: Mirror](character/custommirror.md)
  A mirror that reflects the `Character` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](character/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Character` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/hash(into:))*