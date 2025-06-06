# ==(_:_:)

**Framework**: Apple CryptoKit  
**Kind**: op

Returns a Boolean value indicating whether a message authentication code is equivalent to a collection of binary data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func == <D>(lhs: Self, rhs: D) -> Bool where D : DataProtocol
```

#### Return Value

A Boolean value that’s `true` if the message authentication code and the collection of binary data are equivalent.

## Parameters

- `lhs`: A message authentication code to compare.
- `rhs`: A collection of binary data to compare.

## See Also

- [static func == (Self, Self) -> Bool](messageauthenticationcode/==(_:_:)-b90.md)
  Returns a Boolean value indicating whether two message authentication codes are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/messageauthenticationcode/==(_:_:)-3rxc4)*