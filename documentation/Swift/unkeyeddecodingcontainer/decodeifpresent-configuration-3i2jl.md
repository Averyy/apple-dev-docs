# decodeIfPresent(_:configuration:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
mutating func decodeIfPresent<T, C>(_: T.Type, configuration: C.Type) throws -> T? where T : DecodableWithConfiguration, C : DecodingConfigurationProviding, T.DecodingConfiguration == C.DecodingConfiguration
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decodeifpresent(_:configuration:)-3i2jl)*