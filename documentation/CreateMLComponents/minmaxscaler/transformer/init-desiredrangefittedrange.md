# init(desiredRange:fittedRange:)

**Framework**: Create ML Components  
**Kind**: init

Creates a minmax scaling transformer.

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
init(desiredRange: ClosedRange<Element>, fittedRange: ClosedRange<Element>)
```

## Parameters

- `desiredRange`: The desired range of transformed values.
- `fittedRange`: The range derived by the estimator when fitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/minmaxscaler/transformer/init(desiredrange:fittedrange:))*