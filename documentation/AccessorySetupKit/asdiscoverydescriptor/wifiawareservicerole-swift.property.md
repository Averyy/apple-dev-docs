# wifiAwareServiceRole

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Instance Property

The role of the accessory’s Wi-Fi Aware’s service.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var wifiAwareServiceRole: ASDiscoveryDescriptor.WiFiAwareServiceRole { get set }
```

```objc
@property (nonatomic, assign, readwrite) ASDiscoveryDescriptorWiFiAwareServiceRole wifiAwareServiceRole;
```

## Discussion

This property defaults to [`ASDiscoveryDescriptor.WiFiAwareServiceRole.subscriber`](./wifiawareservicerole-swift.enum/subscriber.md)

## See Also

### Specifying Wi-Fi Aware properties
- [var wifiAwareServiceName: String?](./wifiawareservicename.md)
  The accessory’s Wi-Fi Aware’s service name if available.
- [ASDiscoveryDescriptor.WiFiAwareServiceRole](./wifiawareservicerole-swift.enum.md)
  A type that defines the role of an accessory’s Wi-Fi Aware’s service.
- [var wifiAwareModelNameMatch: ASPropertyCompareString?](./wifiawaremodelnamematch.md)
  The accessory’s Wi-Fi Aware model name and matching options.
- [var wifiAwareVendorNameMatch: ASPropertyCompareString?](./wifiawarevendornamematch.md)
  The accessory’s Wi-Fi Aware vendor name and matching options.
- [class ASPropertyCompareString](../aspropertycomparestring.md)
  A type that specifies how to filter a property against a given string and comparison options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor/wifiawareservicerole-swift.property)*