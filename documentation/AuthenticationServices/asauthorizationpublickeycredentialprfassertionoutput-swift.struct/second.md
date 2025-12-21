# second

**Framework**: Authentication Services  
**Kind**: property

A second symmetric key that’s unique to the passkey, and derives from the second input, if specified.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
let second: SymmetricKey?
```

#### Discussion

If `input2` isn’t specified, this key is `nil`.

## See Also

- [let first: SymmetricKey](asauthorizationpublickeycredentialprfassertionoutput-swift.struct/first.md)
  A symmetric key that’s unique to the passkey and derives from the first input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertionoutput-swift.struct/second)*