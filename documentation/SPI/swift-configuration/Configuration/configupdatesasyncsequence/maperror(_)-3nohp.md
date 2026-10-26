---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/maperror(_:)-3nohp"
framework: "swift-configuration/Configuration"
---

# mapError(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.mapError(_:)`.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func mapError<MappedError>(_ transform: @escaping @Sendable (Self.Failure) -> MappedError) -> some AsyncSequence<Self.Element, MappedError> where MappedError : Error
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/maperror(_:)-3nohp)*