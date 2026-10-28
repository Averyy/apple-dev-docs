# summary(includingStatistics:)

**Framework**: Core AI  
**Kind**: method  
**Role**: Instance Method

Returns the model summary.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func summary(includingStatistics: Bool) throws -> AIModelAsset.Summary?
```

## Return Value

The model summary, or `nil` if no program bytecode exists.

## Parameters

- `includingStatistics`: A Boolean value that indicates whether to read detailed model statistics. If `false`, the summary contains only version information and function signatures. Including model statistics is considerably slower for large models.

## See Also

### Inspecting an asset
- [var metadata: AIModelAsset.Metadata](./metadata-swift.property.md)
  The author-provided metadata for the model asset.
- [let url: URL](./url.md)
  The file URL of the model asset bundle on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/summary(includingstatistics:))*