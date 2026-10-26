# selectionLimit

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The maximum number of selections the user can make.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
var selectionLimit: Int
```

#### Discussion

The default value is `1`. Setting the value to `0` sets the selection limit to the maximum that the system supports.

## See Also

### Setting the selection limit
- [var selection: PHPickerConfiguration.Selection](./selection-swift.property.md)
  The selection behavior for the picker.
- [enum PHPickerConfigurationSelection](../phpickerconfigurationselection.md)
  Options that represent differing selection behavior.
- [PHPickerConfiguration.Selection](./selection-swift.enum.md)
  Options that represent differing selection behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/selectionlimit)*