# init(_:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

Creates a temporal supervised estimator from a supervised estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
init(_ base: Base)
```

## Discussion

The resulting estimator collects all elements of the input sequence before calling fit on the underlying estimator. The transformer returned from fit is also converted to a temporal transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimatortotemporaladaptor/init(_:))*