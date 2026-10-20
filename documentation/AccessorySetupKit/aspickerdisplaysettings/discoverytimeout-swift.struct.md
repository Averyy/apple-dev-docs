# ASPickerDisplaySettings.DiscoveryTimeout

**Framework**: AccessorySetupKit  
**Kind**: struct  
**Role**: Structure

The type used for the accessory picker’s discovery timeout value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct DiscoveryTimeout
```

```c
typedef NSTimeInterval ASPickerDisplaySettingsDiscoveryTimeout;
```

## Topics

### Determining discovery timeout
- [class var `default`: ASPickerDisplaySettings](./default.md)
  An empty settings object.
- [static let short: ASPickerDisplaySettings.DiscoveryTimeout](./discoverytimeout-swift.struct/short.md)
  A picker discovery timeout value that times out after about about 60 seconds.
- [static let medium: ASPickerDisplaySettings.DiscoveryTimeout](./discoverytimeout-swift.struct/medium.md)
  A picker discovery timeout value that times out after about two minutes.
- [static let long: ASPickerDisplaySettings.DiscoveryTimeout](./discoverytimeout-swift.struct/long.md)
  A picker discovery timeout value that times out after about five minutes.
- [static let unbounded: ASPickerDisplaySettings.DiscoveryTimeout](./discoverytimeout-swift.struct/unbounded.md)
  A picker discovery that only times out when the app tells it to.
### Working with raw values
- [init(rawValue: TimeInterval)](./discoverytimeout-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing the discovery timeout
- [var discoveryTimeout: ASPickerDisplaySettings.DiscoveryTimeout](./discoverytimeout-swift.property.md)
  Custom timeout for picker. Default is 30 seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplaysettings/discoverytimeout-swift.struct)*