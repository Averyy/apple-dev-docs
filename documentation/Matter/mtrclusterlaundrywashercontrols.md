# MTRClusterLaundryWasherControls

**Framework**: Matter  
**Kind**: class

Cluster Laundry Washer Controls This cluster supports remotely monitoring and controlling the different types of functionality available to a washing device, such as a washing machine.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class MTRClusterLaundryWasherControls
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterlaundrywashercontrols/init(device:endpointid:queue:).md)
  The queue is currently unused, but may be used in the future for calling completions for command invocations if commands are added to this cluster.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashercontrols/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashercontrols/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashercontrols/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashercontrols/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashercontrols/readattributegeneratedcommandlist(with:).md)
- [func readAttributeNumberOfRinses(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashercontrols/readattributenumberofrinses(with:).md)
- [func readAttributeSpinSpeedCurrent(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashercontrols/readattributespinspeedcurrent(with:).md)
- [func readAttributeSpinSpeeds(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashercontrols/readattributespinspeeds(with:).md)
- [func readAttributeSupportedRinses(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrywashercontrols/readattributesupportedrinses(with:).md)
- [func writeAttributeNumberOfRinses(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlaundrywashercontrols/writeattributenumberofrinses(withvalue:expectedvalueinterval:).md)
- [func writeAttributeNumberOfRinses(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlaundrywashercontrols/writeattributenumberofrinses(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeSpinSpeedCurrent(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlaundrywashercontrols/writeattributespinspeedcurrent(withvalue:expectedvalueinterval:).md)
- [func writeAttributeSpinSpeedCurrent(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlaundrywashercontrols/writeattributespinspeedcurrent(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterlaundrywashercontrols)*