# moveAsset(withIdentifier:afterAssetWithIdentifier:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Reorders assets that are in a selected state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func moveAsset(withIdentifier identifier: String, afterAssetWithIdentifier afterIdentifier: String?)
```

```objc
- (void) moveAssetWithIdentifier:(NSString *) identifier afterAssetWithIdentifier:(NSString *) afterIdentifier;
```

## Discussion

This method ignores assets that are invalid or aren’t in a selected state, and if you don’t specify a library when calling [`init(photoLibrary:)`](../phpickerconfiguration-swift.struct/init%28photolibrary%29.md).

If `afterIdentifier` is `nil`, the identifier you specify moves to the beginning of the picker.

## Parameters

- `identifier`: The identifier that represents the asset to move.
- `afterIdentifier`: The identifier to move the asset to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerviewcontroller/moveasset(withidentifier:afterassetwithidentifier:))*