# MTRClusterLaundryWasherControls

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterLaundryWasherControls : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterlaundrywashercontrols/init%28device,endpointid,queue%29.md)
  The queue is currently unused, but may be used in the future for calling completions for command invocations if commands are added to this cluster.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrywashercontrols/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrywashercontrols/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrywashercontrols/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrywashercontrols/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrywashercontrols/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeNumberOfRinses(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrywashercontrols/readattributenumberofrinses%28with%29.md)
- [func readAttributeSpinSpeedCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrywashercontrols/readattributespinspeedcurrent%28with%29.md)
- [func readAttributeSpinSpeeds(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrywashercontrols/readattributespinspeeds%28with%29.md)
- [func readAttributeSupportedRinses(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrywashercontrols/readattributesupportedrinses%28with%29.md)
- [func writeAttributeNumberOfRinses(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterlaundrywashercontrols/writeattributenumberofrinses%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeNumberOfRinses(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterlaundrywashercontrols/writeattributenumberofrinses%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeSpinSpeedCurrent(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterlaundrywashercontrols/writeattributespinspeedcurrent%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeSpinSpeedCurrent(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterlaundrywashercontrols/writeattributespinspeedcurrent%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterlaundrywashercontrols)*