# getLocalSizeOfAssetPackWithIdentifier:calculationMethod:completionHandler:

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

```objc
- (void) getLocalSizeOfAssetPackWithIdentifier:(NSString *) assetPackIdentifier calculationMethod:(BASizeCalculationMethod) calculationMethod completionHandler:(void (^)(long long size, NSError *error)) completionHandler;
```

#### Discussion

This is different than the download size, which could be smaller. Calculating the size of an asset pack that contains many files can take a long time.

## Parameters

- `assetPackIdentifier`: The asset pack’s identifier.
- `calculationMethod`: The method to use to calculate the asset pack’s installation size.
- `completionHandler`: A block that receives the asset pack’s installation size in bytes or an error if one occurs. If the asset pack isn’t available locally, then the `error` parameter will point to an `NSError` object with [`BAManagedErrorCodeAssetPackNotFound`](../bamanagederrorcode/bamanagederrorcodeassetpacknotfound.md) as its code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/getlocalsizeofassetpackwithidentifier:calculationmethod:completionhandler:)*