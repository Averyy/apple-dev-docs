# MTRClusterLaundryDryerControls

**Framework**: Matter  
**Kind**: class

Cluster Laundry Dryer Controls This cluster provides a way to access options associated with the operation of a laundry dryer device type.

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
class MTRClusterLaundryDryerControls
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterlaundrydryercontrols/init(device:endpointid:queue:).md)
  The queue is currently unused, but may be used in the future for calling completions for command invocations if commands are added to this cluster.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrydryercontrols/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrydryercontrols/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrydryercontrols/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrydryercontrols/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrydryercontrols/readattributegeneratedcommandlist(with:).md)
- [func readAttributeSelectedDrynessLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrydryercontrols/readattributeselecteddrynesslevel(with:).md)
- [func readAttributeSupportedDrynessLevels(with: MTRReadParams?) -> [String : Any]?](mtrclusterlaundrydryercontrols/readattributesupporteddrynesslevels(with:).md)
- [func writeAttributeSelectedDrynessLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterlaundrydryercontrols/writeattributeselecteddrynesslevel(withvalue:expectedvalueinterval:).md)
- [func writeAttributeSelectedDrynessLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterlaundrydryercontrols/writeattributeselecteddrynesslevel(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterlaundrydryercontrols)*