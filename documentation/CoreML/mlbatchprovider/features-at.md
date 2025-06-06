# features(at:)

**Framework**: Core ML  
**Kind**: method  
**Required**: Yes

Returns the feature provider at the given index.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func features(at index: Int) -> any MLFeatureProvider
```

#### Return Value

The feature provider at the given index.

## Parameters

- `index`: The index of the desired feature provider.

## See Also

- [var count: Int](mlbatchprovider/count.md)
  The number of feature providers in this batch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlbatchprovider/features(at:))*