# localSize(ofAssetPackWithID:calculationMethod:)

**Framework**: Background Assets  
**Kind**: method

Calculates a locally available asset pack’s installation size.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)

## Declaration

```swift
func localSize(ofAssetPackWithID assetPackID: String, calculationMethod: SizeCalculationMethod) async throws -> Int64
```

#### Return Value

The asset pack’s installation size in bytes.

#### Discussion

This is different than the download size, which could be smaller. Calculating the size of an asset pack that contains many files can take a long time.

> **Note**: [`ManagedBackgroundAssetsError.assetPackNotFound(withID:)`](managedbackgroundassetserror/assetpacknotfound(withid:).md) when no asset pack with the specified ID is available locally.

## Parameters

- `assetPackID`: The asset pack’s ID.
- `calculationMethod`: The method to use to calculate the asset pack’s installation size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/localsize(ofassetpackwithid:calculationmethod:))*