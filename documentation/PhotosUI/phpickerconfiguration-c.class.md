# PHPickerConfiguration

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

An object that contains information about how to configure a picker view controller.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
@interface PHPickerConfiguration : NSObject
```

## Topics

### Creating a configuration
- [- init](./phpickerconfiguration-c.class/init.md)
  Creates a new configuration object.
- [- initWithPhotoLibrary:](./phpickerconfiguration-c.class/initwithphotolibrary_.md)
  Creates a new configuration object for a photo library.
### Filtering asset types
- [filter](./phpickerconfiguration-c.class/filter.md)
  The filter you apply to restrict the asset types the picker displays.
- [PHPickerFilter](./phpickerfilter-c.class.md)
  A type that defines the filter to apply to the photo library.
### Selecting the preferred asset representation
- [preferredAssetRepresentationMode](./phpickerconfiguration-c.class/preferredassetrepresentationmode.md)
  A mode that determines which representation to use if an asset contains more than one.
- [enum PHPickerConfigurationAssetRepresentationMode](./phpickerconfigurationassetrepresentationmode.md)
  Constants identifying the mode the system uses when many representations exist for an asset.
### Preselecting assets
- [preselectedAssetIdentifiers](./phpickerconfiguration-c.class/preselectedassetidentifiers.md)
  An array of asset identifiers to preselect in the picker.
### Setting the selection limit
- [selectionLimit](./phpickerconfiguration-c.class/selectionlimit.md)
  The maximum number of selections the user can make.
- [selection](./phpickerconfiguration-c.class/selection.md)
  The selection behavior for the picker.
- [enum PHPickerConfigurationSelection](./phpickerconfigurationselection.md)
  Options that represent differing selection behavior.
### Customizing picker appearance and behavior
- [mode](./phpickerconfiguration-c.class/mode.md)
  A layout type for the photos in the picker’s view.
- [PHPickerMode](./phpickermode-c.enum.md)
  Layout options that determine how the picker orders photos visually.
- [disabledCapabilities](./phpickerconfiguration-c.class/disabledcapabilities.md)
  The aspects of a photo picker’s default appearance that your app can disable.
- [struct PHPickerCapabilities](./phpickercapabilities.md)
  Options that customize the look and behavior of the photos picker.
- [edgesWithoutContentMargins](./phpickerconfiguration-c.class/edgeswithoutcontentmargins.md)
  The portions of a photo picker’s perimeter that are borderless.
- [PHPickerUpdateConfiguration](./phpickerupdateconfiguration.md)
  An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.
### Instance Properties
- [metadataOptions](./phpickerconfiguration-c.class/metadataoptions.md)
  Metadata options for the picker. Default is \c PHPickerMetadataOptionsNone.
- [searchText](./phpickerconfiguration-c.class/searchtext.md)
  The search text for the picker. Default is \c nil.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Photos picker for UIKit, AppKit
- [Selecting Photos and Videos in iOS](../PhotoKit/selecting-photos-and-videos-in-ios.md)
  Improve the user experience of finding and selecting assets by using the Photos picker.
- [class PHPickerViewController](./phpickerviewcontroller.md)
  A view controller that provides the user interface for choosing assets from the photo library.
- [PHPickerFilter](./phpickerfilter-c.class.md)
  A type that defines the filter to apply to the photo library.
- [PHPickerResult](./phpickerresult-c.class.md)
  Types that represent a selected asset from a person’s photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-c.class)*