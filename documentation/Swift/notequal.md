# !=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether the two arguments are not equal.

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
func != <T>(lhs: T, rhs: T) -> Bool where T : Equatable, T : RawRepresentable, T.RawValue : Equatable
```

## Parameters

- `lhs`: A raw-representable instance.
- `rhs`: A second raw-representable instance.

## See Also

- [func == <T>(T, T) -> Bool](==(_:_:)-9hu5c.md)
  Returns a Boolean value indicating whether the two arguments are equal.
- [func != <T>(T, T) -> Bool](!=(_:_:)-9wy5n.md)
  Returns a Boolean value indicating whether the two arguments are not equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/!=(_:_:)-8pggn)*