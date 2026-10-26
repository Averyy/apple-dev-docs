# localVersionOfAssetPackWithIdentifier:error:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Returns a locally available asset pack’s version number.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+

## Declaration

```objc
- (NSInteger) localVersionOfAssetPackWithIdentifier:(NSString *) assetPackIdentifier error:(NSError **) error;
```

#### Return Value

The asset pack’s version number. A return value of `-1` indicates that an error occurred.

## Parameters

- `assetPackIdentifier`: The asset pack’s identifier.
- `error`: A pointer to an error that will be set if an error occurs. If the asset pack isn’t available locally, then `error` will point to an `NSError` object with [`BAManagedErrorCodeAssetPackNotFound`](../bamanagederrorcode/bamanagederrorcodeassetpacknotfound.md) as its code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/localversionofassetpackwithidentifier:error:)*