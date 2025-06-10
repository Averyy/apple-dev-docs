# MTRClusterBooleanStateConfiguration

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRClusterBooleanStateConfiguration
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterbooleanstateconfiguration/init(device:endpointid:queue:).md)
### Instance Methods
- [func enableDisableAlarm(with: MTRBooleanStateConfigurationClusterEnableDisableAlarmParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterbooleanstateconfiguration/enabledisablealarm(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAlarmsActive(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributealarmsactive(with:).md)
- [func readAttributeAlarmsEnabled(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributealarmsenabled(with:).md)
- [func readAttributeAlarmsSupported(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributealarmssupported(with:).md)
- [func readAttributeAlarmsSuppressed(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributealarmssuppressed(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentSensitivityLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributecurrentsensitivitylevel(with:).md)
- [func readAttributeDefaultSensitivityLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributedefaultsensitivitylevel(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributegeneratedcommandlist(with:).md)
- [func readAttributeSensorFault(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributesensorfault(with:).md)
- [func readAttributeSupportedSensitivityLevels(with: MTRReadParams?) -> [String : Any]?](mtrclusterbooleanstateconfiguration/readattributesupportedsensitivitylevels(with:).md)
- [func suppressAlarm(with: MTRBooleanStateConfigurationClusterSuppressAlarmParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterbooleanstateconfiguration/suppressalarm(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func writeAttributeCurrentSensitivityLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbooleanstateconfiguration/writeattributecurrentsensitivitylevel(withvalue:expectedvalueinterval:).md)
- [func writeAttributeCurrentSensitivityLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbooleanstateconfiguration/writeattributecurrentsensitivitylevel(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterbooleanstateconfiguration)*