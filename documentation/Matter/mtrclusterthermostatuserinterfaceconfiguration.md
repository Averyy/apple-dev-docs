# MTRClusterThermostatUserInterfaceConfiguration

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
class MTRClusterThermostatUserInterfaceConfiguration
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterthermostatuserinterfaceconfiguration/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterthermostatuserinterfaceconfiguration/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthermostatuserinterfaceconfiguration/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthermostatuserinterfaceconfiguration/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterthermostatuserinterfaceconfiguration/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterthermostatuserinterfaceconfiguration/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthermostatuserinterfaceconfiguration/readattributegeneratedcommandlist(with:).md)
- [func readAttributeKeypadLockout(with: MTRReadParams?) -> [String : Any]?](mtrclusterthermostatuserinterfaceconfiguration/readattributekeypadlockout(with:).md)
- [func readAttributeScheduleProgrammingVisibility(with: MTRReadParams?) -> [String : Any]?](mtrclusterthermostatuserinterfaceconfiguration/readattributescheduleprogrammingvisibility(with:).md)
- [func readAttributeTemperatureDisplayMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterthermostatuserinterfaceconfiguration/readattributetemperaturedisplaymode(with:).md)
- [func writeAttributeKeypadLockout(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout(withvalue:expectedvalueinterval:).md)
- [func writeAttributeKeypadLockout(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterthermostatuserinterfaceconfiguration/writeattributekeypadlockout(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility(withvalue:expectedvalueinterval:).md)
- [func writeAttributeScheduleProgrammingVisibility(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterthermostatuserinterfaceconfiguration/writeattributescheduleprogrammingvisibility(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeTemperatureDisplayMode(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode(withvalue:expectedvalueinterval:).md)
- [func writeAttributeTemperatureDisplayMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterthermostatuserinterfaceconfiguration/writeattributetemperaturedisplaymode(withvalue:expectedvalueinterval:params:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterthermostatuserinterfaceconfiguration)*