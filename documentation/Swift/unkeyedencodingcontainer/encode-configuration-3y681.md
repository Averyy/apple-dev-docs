# encode(_:configuration:)

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
mutating func encode<T, C>(_ t: T, configuration: C.Type) throws where T : EncodableWithConfiguration, C : EncodingConfigurationProviding, T.EncodingConfiguration == C.EncodingConfiguration
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(_:configuration:)-3y681)*