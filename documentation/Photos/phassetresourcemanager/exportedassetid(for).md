# exportedAssetID(for:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns the exported asset ID for the specified asset resource.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func exportedAssetID(for resource: PHAssetResource) async throws -> CKAsset.ExportedAssetID
```

## Return Value

The exported asset ID for the resource.

## Discussion

The returned `CKAsset.ExportedAssetID` can be used to create a `CKAsset` that references the asset resource data without copying it. Network access is always required.

An exported asset ID exists only for a resource whose data iCloud Photos stores in CloudKit as its own `CKAsset`, e.g. the original media and adjustment renders in `PHAssetResource/TypeGroups/coreComponents`, and `PHAssetResourceType/derivative` resources in `PHAssetResource/TypeGroups/mediaDerivatives`.

Resources that have no CloudKit asset to reference, like the on-device generated `PHAssetResourceType/thumbnailDerivative`, will fail with [`missingResource`](../phphotoserror-swift.struct/missingresource.md).

Note that a resource’s [`type`](../phassetresource/type.md) alone does not determine whether an ID is available — a library that stopped using iCloud Photos may still report resources of a referenceable type. Request an ID for the specific resource you intend to reference, and fall back to requesting the resource’s data when none is available.

The photo library must use iCloud Photos; a request against a library that doesn’t fails with [`requestNotSupportedForAsset`](../phphotoserror-swift.struct/requestnotsupportedforasset.md).

This method supports task cancellation. If the calling task is cancelled, the underlying network request is cancelled and this method throws `CancellationError`.

> **Throws**: [`missingResource`](../phphotoserror-swift.struct/missingresource.md) if the resource has no CloudKit asset to reference, `CancellationError` if the task is cancelled, or another error if the request fails.

## Parameters

- `resource`: The asset resource to get an exported asset ID for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcemanager/exportedassetid(for:))*