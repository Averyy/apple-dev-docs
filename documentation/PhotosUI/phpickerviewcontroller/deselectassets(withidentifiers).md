# deselectAssets(withIdentifiers:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Deselects assets that are in a selected state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func deselectAssets(withIdentifiers identifiers: [String])
```

```objc
- (void) deselectAssetsWithIdentifiers:(NSArray<NSString *> *) identifiers;
```

## Discussion

This method ignores assets that are invalid or aren’t in a selected state, and if you don’t specify a library when calling [`init(photoLibrary:)`](../phpickerconfiguration-swift.struct/init%28photolibrary%29.md).

## Parameters

- `identifiers`: The list of identifiers to deselect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerviewcontroller/deselectassets(withidentifiers:))*