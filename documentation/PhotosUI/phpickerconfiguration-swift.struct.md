# PHPickerConfiguration

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

An object that contains information about how to configure a picker view controller.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
struct PHPickerConfiguration
```

## Topics

### Creating a configuration
- [init()](./phpickerconfiguration-swift.struct/init%28%29.md)
  Creates a new configuration object.
- [init(photoLibrary: PHPhotoLibrary)](./phpickerconfiguration-swift.struct/init%28photolibrary%29.md)
  Creates a new configuration object for a photo library.
### Filtering asset types
- [var filter: PHPickerFilter?](./phpickerconfiguration-swift.struct/filter.md)
  The filter you apply to restrict the asset types the picker displays.
- [struct PHPickerFilter](./phpickerfilter-swift.struct.md)
  A type that defines the filter to apply to the photo library.
### Selecting the preferred asset representation
- [var preferredAssetRepresentationMode: PHPickerConfiguration.AssetRepresentationMode](./phpickerconfiguration-swift.struct/preferredassetrepresentationmode.md)
  A mode that determines which representation to use if an asset contains more than one.
- [PHPickerConfiguration.AssetRepresentationMode](./phpickerconfiguration-swift.struct/assetrepresentationmode.md)
  Constants identifying the mode the system uses when many representations exist for an asset.
### Preselecting assets
- [var preselectedAssetIdentifiers: [String]](./phpickerconfiguration-swift.struct/preselectedassetidentifiers.md)
  An array of asset identifiers to preselect in the picker.
### Setting the selection limit
- [var selectionLimit: Int](./phpickerconfiguration-swift.struct/selectionlimit.md)
  The maximum number of selections the user can make.
- [var selection: PHPickerConfiguration.Selection](./phpickerconfiguration-swift.struct/selection-swift.property.md)
  The selection behavior for the picker.
- [enum PHPickerConfigurationSelection](./phpickerconfigurationselection.md)
  Options that represent differing selection behavior.
- [PHPickerConfiguration.Selection](./phpickerconfiguration-swift.struct/selection-swift.enum.md)
  Options that represent differing selection behavior.
### Customizing picker appearance and behavior
- [var mode: PHPickerMode](./phpickerconfiguration-swift.struct/mode.md)
  A layout type for the photos in the picker’s view.
- [struct PHPickerMode](./phpickermode-swift.struct.md)
  Layout options that determine how the picker orders photos visually.
- [var disabledCapabilities: PHPickerCapabilities](./phpickerconfiguration-swift.struct/disabledcapabilities.md)
  The aspects of a photo picker’s default appearance that your app can disable.
- [struct PHPickerCapabilities](./phpickercapabilities.md)
  Options that customize the look and behavior of the photos picker.
- [var edgesWithoutContentMargins: NSDirectionalRectEdge](./phpickerconfiguration-swift.struct/edgeswithoutcontentmargins.md)
  The portions of a photo picker’s perimeter that are borderless.
- [PHPickerConfiguration.Update](./phpickerconfiguration-swift.struct/update.md)
  An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.
### Instance Properties
- [var metadataOptions: PHPickerMetadataOptions](./phpickerconfiguration-swift.struct/metadataoptions.md)
  Metadata options for the picker. Default is `[]`.
- [var searchText: PHPickerSearchText?](./phpickerconfiguration-swift.struct/searchtext.md)
  The search text for the picker. Default is `nil`.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Photos picker for UIKit, AppKit
- [Selecting Photos and Videos in iOS](../PhotoKit/selecting-photos-and-videos-in-ios.md)
  Improve the user experience of finding and selecting assets by using the Photos picker.
- [class PHPickerViewController](./phpickerviewcontroller.md)
  A view controller that provides the user interface for choosing assets from the photo library.
- [protocol PHPickerViewControllerDelegate](./phpickerviewcontrollerdelegate-5yntc.md)
  A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [struct PHPickerFilter](./phpickerfilter-swift.struct.md)
  A type that defines the filter to apply to the photo library.
- [struct PHPickerResult](./phpickerresult-swift.struct.md)
  Types that represent a selected asset from a person’s photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct)*