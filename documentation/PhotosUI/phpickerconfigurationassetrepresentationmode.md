# PHPickerConfigurationAssetRepresentationMode

**Framework**: PhotosUI  
**Kind**: enum  
**Role**: Enumeration

Constants identifying the mode the system uses when many representations exist for an asset.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum PHPickerConfigurationAssetRepresentationMode
```

```c
enum PHPickerConfigurationAssetRepresentationMode : NSInteger;
```

## Topics

### Constants
- [PHPickerConfigurationAssetRepresentationMode.automatic](./phpickerconfigurationassetrepresentationmode/automatic.md)
  A mode that indicates that the system chooses the appropriate asset representation.
- [PHPickerConfigurationAssetRepresentationMode.compatible](./phpickerconfigurationassetrepresentationmode/compatible.md)
  A mode that uses the most compatible asset representation.
- [PHPickerConfigurationAssetRepresentationMode.current](./phpickerconfigurationassetrepresentationmode/current.md)
  A mode that uses the current representation to avoid transcoding, if possible.
### Initializers
- [init?(rawValue: Int)](./phpickerconfigurationassetrepresentationmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Selecting the preferred asset representation
- [preferredAssetRepresentationMode](./phpickerconfiguration-c.class/preferredassetrepresentationmode.md)
  A mode that determines which representation to use if an asset contains more than one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfigurationassetrepresentationmode)*