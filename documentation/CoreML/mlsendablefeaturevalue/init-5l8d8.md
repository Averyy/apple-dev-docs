# init(_:)

**Framework**: Core ML  
**Kind**: init

Creates a sendable feature value from a feature value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init?(_ value: MLFeatureValue)
```

#### Discussion

Some feature values are not representable as a sendable values. In those cases this initializer will return `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsendablefeaturevalue/init(_:)-5l8d8)*