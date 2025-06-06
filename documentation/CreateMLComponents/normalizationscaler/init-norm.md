# init(norm:)

**Framework**: Create ML Components  
**Kind**: init

Creates a normalization scaler.

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
init(norm: NormalizationScaler<Element>.NormalizationStrategy = .l2)
```

## Parameters

- `norm`: A selected NormalizationStrategy to scale by. Defaults as  .

## See Also

- [NormalizationScaler.NormalizationStrategy](normalizationscaler/normalizationstrategy.md)
  A normalization strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/normalizationscaler/init(norm:))*