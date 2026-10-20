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

Available when `Wrapped` conforms to `Hashable`.

## Parameters

- `hasher`: The hasher to use when combining the components of this instance.

## See Also

### Inspecting an Optional
- [var unsafelyUnwrapped: Wrapped](./unsafelyunwrapped.md)
  The wrapped value of this instance, unwrapped without checking whether the instance is `nil`.
- [var debugDescription: String](./debugdescription.md)
  A textual representation of this instance, suitable for debugging.
- [var customMirror: Mirror](./custommirror.md)
  The custom mirror for this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/hash(into:))*