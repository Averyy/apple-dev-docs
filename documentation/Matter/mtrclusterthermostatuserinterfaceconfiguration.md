# MTRClusterThermostatUserInterfaceConfiguration

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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
class MTRClusterThermostatUserInterfaceConfiguration
```

```objc
@interface MTRClusterThermostatUserInterfaceConfiguration : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterthermostatuserinterfaceconfiguration/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterthermostatuserinterfaceconfiguration/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostatuserinterfaceconfiguration/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostatuserinterfaceconfiguration/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostatuserinterfaceconfiguration/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostatuserinterfaceconfiguration/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostatuserinterfaceconfiguration/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeKeypadLockout(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostatuserinterfaceconfiguration/readattributekeypadlockout%28with%29.md)
- [func readAttributeScheduleProgrammingVisibility(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostatuserinterfaceconfiguration/readattributescheduleprogrammingvisibility%28with%29.md)
- [func readAttributeTemperatureDisplayMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostatuserinterfaceconfiguration/readattributetemperaturedisplaymode%28with%29.md)
- [func writeAttributeKeypadLockout(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeKeypadLockout(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeTemperatureDisplayMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeTemperatureDisplayMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode%28withvalue,expectedvalueinterval,params%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterthermostatuserinterfaceconfiguration)*