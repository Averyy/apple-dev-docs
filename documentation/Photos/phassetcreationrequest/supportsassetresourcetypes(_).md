# supportsAssetResourceTypes(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value indicating whether Photos supports creating an asset with the specified combination of resource types.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func supportsAssetResourceTypes(_ types: [NSNumber]) -> Bool
```

```objc
+ (BOOL) supportsAssetResourceTypes:(NSArray<NSNumber *> *) types;
```

## Return Value

`true` if Photos supports the specified combination of resource types; otherwise, `false`.

## Discussion

When you request creation of an asset from resource data, Photos does not validate that the resources can construct a complete asset until the complete [`PHPhotoLibrary`](../phphotolibrary.md) [`performChanges(_:completionHandler:)`](../phphotolibrary/performchanges%28_,completionhandler%29.md) change block executes. (If an asset cannot be constructed from the provided resources, Photos calls the `completionHandler` you provide in that method with an error describing the failure.) To perform preflight validation before executing an asset creation request, use this method to verify that the set of resource types from which you want to create an asset are correct.

This method verifies only that the collection of asset resource types is valid (for example, ensuring that you do not attempt to construct a photo asset without image data), so it is still possible for an asset creation request to fail if the data itself is incomplete or invalid. However, calling by using this method you can avoid some kinds of asset creation failure before performing the expensive operation of reading (and potentially downloading or transmitting) asset resource data.

## Parameters

- `types`: An array of numbers, each the raw value of a [`PHAssetResourceType`](../phassetresourcetype.md) identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcreationrequest/supportsassetresourcetypes(_:))*