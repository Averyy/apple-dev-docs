# ASPickerDisplaySettings

**Framework**: AccessorySetupKit  
**Kind**: class

A type that contains settings to customize the display of the accessory picker

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class ASPickerDisplaySettings
```

## Topics

### Accessing the default instance
- [class var `default`: ASPickerDisplaySettings](aspickerdisplaysettings/default.md)
  An empty settings object.
### Customizing the discovery timeout
- [var discoveryTimeout: ASPickerDisplaySettings.DiscoveryTimeout](aspickerdisplaysettings/discoverytimeout-swift.property.md)
  Custom timeout for picker. Default is 30 seconds.
- [ASPickerDisplaySettings.DiscoveryTimeout](aspickerdisplaysettings/discoverytimeout-swift.struct.md)
  The type used for the accessory picker’s discovery timeout value.
### Customizing picker options
- [var options: ASPickerDisplaySettings.Options](aspickerdisplaysettings/options-swift.property.md)
  Custom options for the picker.
- [ASPickerDisplaySettings.Options](aspickerdisplaysettings/options-swift.struct.md)
  Options offered by the accessory picker.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var pickerDisplaySettings: ASPickerDisplaySettings?](asaccessorysession/pickerdisplaysettings.md)
  Settings that affect the display of the accessory picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplaysettings)*