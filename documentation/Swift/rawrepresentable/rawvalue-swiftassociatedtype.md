# RawValue

**Framework**: Swift  
**Kind**: associatedtype  
**Required**: Yes

The raw type that can be used to represent all values of the conforming type.

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
associatedtype RawValue
```

#### Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.

## See Also

- [var rawValue: Self.RawValue](rawrepresentable/rawvalue-swift.property.md)
  The corresponding value of the raw type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawrepresentable/rawvalue-swift.associatedtype)*