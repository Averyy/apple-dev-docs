# init(charactersIn:)

**Framework**: Foundation  
**Kind**: init

Initialize with a range of integers.

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
init(charactersIn range: Range<Unicode.Scalar>)
```

#### Discussion

It is the caller’s responsibility to ensure that the values represent valid `Unicode.Scalar` values, if that is what is desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/characterset/init(charactersin:)-8tcll)*