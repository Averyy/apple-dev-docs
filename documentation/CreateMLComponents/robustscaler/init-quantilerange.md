# init(quantileRange:)

**Framework**: Create ML Components  
**Kind**: init

Creates a robust scaler.

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
init(quantileRange: ClosedRange<Element> = 0.25...0.75)
```

## Parameters

- `quantileRange`: This scaler removes the median and scales the data according to the quantile range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/robustscaler/init(quantilerange:))*