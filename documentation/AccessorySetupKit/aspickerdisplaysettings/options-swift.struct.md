# ASPickerDisplaySettings.Options

**Framework**: AccessorySetupKit  
**Kind**: struct  
**Role**: Structure

Options offered by the accessory picker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct Options
```

```c
enum ASPickerDisplaySettingsOptions : NSUInteger;
```

## Topics

### Working with filter options
- [static var filterDiscoveryResults: ASPickerDisplaySettings.Options](./options-swift.struct/filterdiscoveryresults.md)
  An option to pass discovered accessories to the app for more custom filtering, before they’re displayed in the picker for selection.
### Initializers
- [init(rawValue: UInt)](./options-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Customizing picker options
- [var options: ASPickerDisplaySettings.Options](./options-swift.property.md)
  Custom options for the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplaysettings/options-swift.struct)*