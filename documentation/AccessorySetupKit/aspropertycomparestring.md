# ASPropertyCompareString

**Framework**: AccessorySetupKit  
**Kind**: class  
**Role**: Class

A type that specifies how to filter a property against a given string and comparison options.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class ASPropertyCompareString
```

```objc
@interface ASPropertyCompareString : NSObject
```

## Topics

### Creating a compare string instance
- [init(string: String, compareOptions: NSString.CompareOptions)](./aspropertycomparestring/init%28string,compareoptions%29.md)
  Creates a property compare string instance with the given string and comparison options.
### Accessing compare string properties
- [var string: String](./aspropertycomparestring/string.md)
  The string to compare against.
- [var compareOptions: NSString.CompareOptions](./aspropertycomparestring/compareoptions.md)
  Comparison options to apply when comparing strings.

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

### Specifying Wi-Fi Aware properties
- [var wifiAwareServiceName: String?](./asdiscoverydescriptor/wifiawareservicename.md)
  The accessory’s Wi-Fi Aware’s service name if available.
- [var wifiAwareServiceRole: ASDiscoveryDescriptor.WiFiAwareServiceRole](./asdiscoverydescriptor/wifiawareservicerole-swift.property.md)
  The role of the accessory’s Wi-Fi Aware’s service.
- [ASDiscoveryDescriptor.WiFiAwareServiceRole](./asdiscoverydescriptor/wifiawareservicerole-swift.enum.md)
  A type that defines the role of an accessory’s Wi-Fi Aware’s service.
- [var wifiAwareModelNameMatch: ASPropertyCompareString?](./asdiscoverydescriptor/wifiawaremodelnamematch.md)
  The accessory’s Wi-Fi Aware model name and matching options.
- [var wifiAwareVendorNameMatch: ASPropertyCompareString?](./asdiscoverydescriptor/wifiawarevendornamematch.md)
  The accessory’s Wi-Fi Aware vendor name and matching options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspropertycomparestring)*