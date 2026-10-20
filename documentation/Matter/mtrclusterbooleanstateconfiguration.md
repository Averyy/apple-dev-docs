# MTRClusterBooleanStateConfiguration

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterBooleanStateConfiguration : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterbooleanstateconfiguration/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func enableDisableAlarm(with: MTRBooleanStateConfigurationClusterEnableDisableAlarmParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterbooleanstateconfiguration/enabledisablealarm%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAlarmsActive(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributealarmsactive%28with%29.md)
- [func readAttributeAlarmsEnabled(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributealarmsenabled%28with%29.md)
- [func readAttributeAlarmsSupported(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributealarmssupported%28with%29.md)
- [func readAttributeAlarmsSuppressed(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributealarmssuppressed%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentSensitivityLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributecurrentsensitivitylevel%28with%29.md)
- [func readAttributeDefaultSensitivityLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributedefaultsensitivitylevel%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeSensorFault(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributesensorfault%28with%29.md)
- [func readAttributeSupportedSensitivityLevels(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbooleanstateconfiguration/readattributesupportedsensitivitylevels%28with%29.md)
- [func suppressAlarm(with: MTRBooleanStateConfigurationClusterSuppressAlarmParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterbooleanstateconfiguration/suppressalarm%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func writeAttributeCurrentSensitivityLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbooleanstateconfiguration/writeattributecurrentsensitivitylevel%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeCurrentSensitivityLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbooleanstateconfiguration/writeattributecurrentsensitivitylevel%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterbooleanstateconfiguration)*