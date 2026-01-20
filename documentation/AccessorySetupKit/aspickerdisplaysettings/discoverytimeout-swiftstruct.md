# ASPickerDisplaySettings.DiscoveryTimeout

**Framework**: AccessorySetupKit  
**Kind**: struct

The type used for the accessory picker’s discovery timeout value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct DiscoveryTimeout
```

## Topics

### Determining discovery timeout
- [class var `default`: ASPickerDisplaySettings](aspickerdisplaysettings/default.md)
  An empty settings object.
- [static let short: ASPickerDisplaySettings.DiscoveryTimeout](aspickerdisplaysettings/discoverytimeout-swift.struct/short.md)
  A picker discovery timeout value that times out after about about 60 seconds.
- [static let medium: ASPickerDisplaySettings.DiscoveryTimeout](aspickerdisplaysettings/discoverytimeout-swift.struct/medium.md)
  A picker discovery timeout value that times out after about two minutes.
- [static let long: ASPickerDisplaySettings.DiscoveryTimeout](aspickerdisplaysettings/discoverytimeout-swift.struct/long.md)
  A picker discovery timeout value that times out after about five minutes.
- [static let unbounded: ASPickerDisplaySettings.DiscoveryTimeout](aspickerdisplaysettings/discoverytimeout-swift.struct/unbounded.md)
  A picker discovery that only times out when the app tells it to.
### Working with raw values
- [init(rawValue: TimeInterval)](aspickerdisplaysettings/discoverytimeout-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var discoveryTimeout: ASPickerDisplaySettings.DiscoveryTimeout](aspickerdisplaysettings/discoverytimeout-swift.property.md)
  Custom timeout for picker. Default is 30 seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplaysettings/discoverytimeout-swift.struct)*