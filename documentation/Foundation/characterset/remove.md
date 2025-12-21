# remove(_:)

**Framework**: Foundation  
**Kind**: method

Remove a `Unicode.Scalar` representation of a character from the `CharacterSet`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@discardableResult
mutating func remove(_ character: Unicode.Scalar) -> Unicode.Scalar?
```

#### Discussion

`Unicode.Scalar` values are available on `Swift.String.UnicodeScalarView`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/characterset/remove(_:))*