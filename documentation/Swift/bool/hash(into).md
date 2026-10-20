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

## Parameters

- `hasher`: The hasher to use when combining the components of this instance.

## See Also

### Inspecting a Boolean
- [var customMirror: Mirror](./custommirror.md)
  A mirror that reflects the `Bool` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./customplaygroundquicklook.md)
  A custom playground Quick Look for the `Bool` instance.
- [var hashValue: Int](./hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bool/hash(into:))*