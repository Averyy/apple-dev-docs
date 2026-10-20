# localSize(ofAssetPackWithID:calculationMethod:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Calculates a locally available asset pack’s installation size.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+

## Declaration

```swift
func localSize(ofAssetPackWithID assetPackID: String, calculationMethod: SizeCalculationMethod) async throws -> Int64
```

#### Return Value

The asset pack’s installation size in bytes.

#### Discussion

This is different than the download size, which could be smaller. Calculating the size of an asset pack that contains many files can take a long time.

> **Throws**: [`ManagedBackgroundAssetsError.assetPackNotFound(withID:)`](../managedbackgroundassetserror/assetpacknotfound%28withid%29.md) when no asset pack with the specified ID is available locally.

## Parameters

- `assetPackID`: The asset pack’s ID.
- `calculationMethod`: The method to use to calculate the asset pack’s installation size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/localsize(ofassetpackwithid:calculationmethod:))*