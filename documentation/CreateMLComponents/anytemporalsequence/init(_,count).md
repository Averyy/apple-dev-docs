# init(_:count:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
init<S>(_ sequence: S, count: Int?) where S : AsyncSequence, S.Element == TemporalFeature<Feature>
```

## See Also

### Creating a sequence
- [init<S>(S)](./init%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/anytemporalsequence/init(_:count:))*