# ASPickerDisplaySettings

**Framework**: AccessorySetupKit  
**Kind**: class  
**Role**: Class

A type that contains settings to customize the display of the accessory picker

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class ASPickerDisplaySettings
```

```objc
@interface ASPickerDisplaySettings : NSObject
```

## Topics

### Accessing the default instance
- [class var `default`: ASPickerDisplaySettings](./aspickerdisplaysettings/default.md)
  An empty settings object.
### Customizing the discovery timeout
- [var discoveryTimeout: ASPickerDisplaySettings.DiscoveryTimeout](./aspickerdisplaysettings/discoverytimeout-swift.property.md)
  Custom timeout for picker. Default is 30 seconds.
- [ASPickerDisplaySettings.DiscoveryTimeout](./aspickerdisplaysettings/discoverytimeout-swift.struct.md)
  The type used for the accessory picker’s discovery timeout value.
### Customizing picker options
- [var options: ASPickerDisplaySettings.Options](./aspickerdisplaysettings/options-swift.property.md)
  Custom options for the picker.
- [ASPickerDisplaySettings.Options](./aspickerdisplaysettings/options-swift.struct.md)
  Options offered by the accessory picker.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Customizing picker behavior
- [var pickerDisplaySettings: ASPickerDisplaySettings?](./asaccessorysession/pickerdisplaysettings.md)
  Settings that affect the display of the accessory picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplaysettings)*