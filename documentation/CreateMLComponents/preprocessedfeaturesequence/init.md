# init(_:)

**Framework**: Create ML Components  
**Kind**: init

Creates an asynchronous sequence of stored temporal features.

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
init<S>(_ sequence: S) async throws where Feature == S.Feature, S : TemporalSequence
```

## Parameters

- `sequence`: An asynchronous sequence of temporal features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessedfeaturesequence/init(_:))*