# NEFilterProviderConfiguration

**Framework**: Network Extension  
**Kind**: class

Configuration parameters for a content filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class NEFilterProviderConfiguration
```

## Topics

### Configuring filter behavior
- [var filterBrowsers: Bool](nefilterproviderconfiguration/filterbrowsers.md)
  A Boolean value that indicates that the system applies the filter to flows of network data originated from WebKit browser objects.
- [var filterSockets: Bool](nefilterproviderconfiguration/filtersockets.md)
  A Boolean value that indicates that the system applies the filter to flows of network data originated from sockets.
- [var filterPackets: Bool](nefilterproviderconfiguration/filterpackets.md)
  A Boolean value that indicates that the system applies the filter to packets of network data.
### Accessing the filter configuration
- [var vendorConfiguration: [String : Any]?](nefilterproviderconfiguration/vendorconfiguration.md)
  A dictionary of provider-specific configuration settings.
- [var serverAddress: String?](nefilterproviderconfiguration/serveraddress.md)
  The address of a server that the Filter Control Provider may contact for rules and other configuration information.
- [var username: String?](nefilterproviderconfiguration/username.md)
  A string that identifies the user.
- [var organization: String?](nefilterproviderconfiguration/organization.md)
  A string that identifies the organization that administers the filter.
- [var passwordReference: Data?](nefilterproviderconfiguration/passwordreference.md)
  A persistent reference to a keychain item containing a password associated with the filter.
- [var identityReference: Data?](nefilterproviderconfiguration/identityreference.md)
  A persistent reference to a keychain item containing a certificate and private key associated with the filter.
### Accessing bundle identifiers
- [var filterDataProviderBundleIdentifier: String?](nefilterproviderconfiguration/filterdataproviderbundleidentifier.md)
  The bundle identifier of the filter data provider system extension.
- [var filterPacketProviderBundleIdentifier: String?](nefilterproviderconfiguration/filterpacketproviderbundleidentifier.md)
  The bundle identifier of the filter packet provider system extension.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NEFilterManager](nefiltermanager.md)
  An object to create and manage a content filter’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration)*