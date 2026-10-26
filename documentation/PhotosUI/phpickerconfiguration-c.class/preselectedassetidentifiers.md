# preselectedAssetIdentifiers

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An array of asset identifiers to preselect in the picker.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy) NSArray<NSString *> * preselectedAssetIdentifiers;
```

#### Discussion

Preselection works only when initializing a [`PHPickerConfiguration`](../phpickerconfiguration-swift.struct.md) object with a photo library. Otherwise, the system returns an error.

The number of preselected asset identifiers can exceed your selection limit. The system disables the done action until the selection count becomes lower than [`selectionLimit`](../phpickerconfiguration-swift.struct/selectionlimit.md).

Additionally, when providing preselected identifiers:

- Results include all preselected identifiers when canceling the picker.
- Results don’t include item providers for preselected assets that remain selected.
- When deselecting all assets, the system keeps the done action enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-c.class/preselectedassetidentifiers)*