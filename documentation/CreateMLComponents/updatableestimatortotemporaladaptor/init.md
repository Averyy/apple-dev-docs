# init(_:)

**Framework**: Create ML Components  
**Kind**: init

Creates a temporal estimator from an estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(_ base: Base)
```

#### Discussion

The resulting estimator collects all elements of the input sequence before calling fit on the underlying estimator. The transformer returned from fit is also converted to a temporal transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortotemporaladaptor/init(_:))*