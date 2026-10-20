# ASDiscoveryDescriptor.WiFiAwareServiceRole

**Framework**: AccessorySetupKit  
**Kind**: enum  
**Role**: Enumeration

A type that defines the role of an accessory’s Wi-Fi Aware’s service.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum WiFiAwareServiceRole
```

```c
enum ASDiscoveryDescriptorWiFiAwareServiceRole : NSInteger;
```

## Topics

### Determining service role
- [ASDiscoveryDescriptor.WiFiAwareServiceRole.subscriber](./wifiawareservicerole-swift.enum/subscriber.md)
  The subscriber service role.
- [ASDiscoveryDescriptor.WiFiAwareServiceRole.publisher](./wifiawareservicerole-swift.enum/publisher.md)
  The publisher service role.
### Working with raw values
- [init?(rawValue: Int)](./wifiawareservicerole-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying Wi-Fi Aware properties
- [var wifiAwareServiceName: String?](./wifiawareservicename.md)
  The accessory’s Wi-Fi Aware’s service name if available.
- [var wifiAwareServiceRole: ASDiscoveryDescriptor.WiFiAwareServiceRole](./wifiawareservicerole-swift.property.md)
  The role of the accessory’s Wi-Fi Aware’s service.
- [var wifiAwareModelNameMatch: ASPropertyCompareString?](./wifiawaremodelnamematch.md)
  The accessory’s Wi-Fi Aware model name and matching options.
- [var wifiAwareVendorNameMatch: ASPropertyCompareString?](./wifiawarevendornamematch.md)
  The accessory’s Wi-Fi Aware vendor name and matching options.
- [class ASPropertyCompareString](../aspropertycomparestring.md)
  A type that specifies how to filter a property against a given string and comparison options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor/wifiawareservicerole-swift.enum)*