# MTRCommissioningParameters

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRCommissioningParameters
```

## Topics

### Instance Properties
- [var attestationNonce: Data?](mtrcommissioningparameters/attestationnonce.md)
- [var countryCode: String?](mtrcommissioningparameters/countrycode.md)
- [var csrNonce: Data?](mtrcommissioningparameters/csrnonce-9eaxq.md)
- [var deviceAttestationDelegate: (any MTRDeviceAttestationDelegate)?](mtrcommissioningparameters/deviceattestationdelegate.md)
- [var failSafeExpiryTimeoutSecs: NSNumber?](mtrcommissioningparameters/failsafeexpirytimeoutsecs.md)
- [var failSafeTimeout: NSNumber?](mtrcommissioningparameters/failsafetimeout.md)
- [var skipCommissioningComplete: Bool](mtrcommissioningparameters/skipcommissioningcomplete.md)
- [var threadOperationalDataset: Data?](mtrcommissioningparameters/threadoperationaldataset.md)
- [var wifiCredentials: Data?](mtrcommissioningparameters/wificredentials.md)
- [var wifiSSID: Data?](mtrcommissioningparameters/wifissid.md)
- [var csrNonce: Data?](mtrcommissioningparameters/csrnonce-8gx94.md)
- [var extraAttributesToRead: [MTRAttributeRequestPath]?](mtrcommissioningparameters/extraattributestoread.md)
  List of attribute paths to read from the commissionee (in addition to whatever attributes are already read to handle readEndpointInformation being YES, or to handle other commissioning tasks).
- [var forceThreadScan: Bool](mtrcommissioningparameters/forcethreadscan.md)
  Whether to force a network scan before requesting Thread credentials. The default is NO.
- [var forceWiFiScan: Bool](mtrcommissioningparameters/forcewifiscan.md)
  Whether to force a network scan before requesting Wi-Fi credentials. The default is NO.
- [var readEndpointInformation: Bool](mtrcommissioningparameters/readendpointinformation.md)
  Read device type information from all endpoints during commissioning. Defaults to NO.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningparameters)*