# THCredentials

**Framework**: ThreadNetwork  
**Kind**: class

A class that contains credentials for a Thread network.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class THCredentials
```

#### Overview

A Thread network defines parameters that all connected devices use. [`THCredentials`](thcredentials.md) provides these parameters.

## Topics

### Getting the Thread Parameters
- [var activeOperationalDataSet: Data?](thcredentials/activeoperationaldataset.md)
  The essential operational parameters for the Thread network.
- [var borderAgentID: Data?](thcredentials/borderagentid.md)
  The identifier of an active Thread network Border Agent.
- [var channel: UInt8](thcredentials/channel.md)
  The Thread network radio channel.
- [var extendedPANID: Data?](thcredentials/extendedpanid.md)
  The Thread network extended PAN identifier.
- [var networkKey: Data?](thcredentials/networkkey.md)
  The Thread network key.
- [var networkName: String?](thcredentials/networkname.md)
  The Thread network name.
- [var panID: Data?](thcredentials/panid.md)
  The Thread network PAN identifier.
- [var pskc: Data?](thcredentials/pskc.md)
  The Thread network pre-shared key (PSKC) for the Commissioner.
### Getting the Framework Parameters
- [var creationDate: Date?](thcredentials/creationdate.md)
  The date and time that the framework stored the credential in the database.
- [var lastModificationDate: Date?](thcredentials/lastmodificationdate.md)
  The date and time that the framework updated the credential in the database.

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [com.apple.developer.networking.manage-thread-network-credentials](../BundleResources/Entitlements/com.apple.developer.networking.manage-thread-network-credentials.md)
  A Boolean value that indicates whether the app can use ThreadNetwork.
- [class THClient](thclient.md)
  A class that supports safely sharing Thread credentials between multiple clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thcredentials)*