# MTRClusterLaundryDryerControls

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterLaundryDryerControls : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterlaundrydryercontrols/init%28device,endpointid,queue%29.md)
  The queue is currently unused, but may be used in the future for calling completions for command invocations if commands are added to this cluster.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrydryercontrols/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrydryercontrols/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrydryercontrols/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrydryercontrols/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrydryercontrols/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeSelectedDrynessLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrydryercontrols/readattributeselecteddrynesslevel%28with%29.md)
- [func readAttributeSupportedDrynessLevels(with: MTRReadParams?) -> [String : Any]?](./mtrclusterlaundrydryercontrols/readattributesupporteddrynesslevels%28with%29.md)
- [func writeAttributeSelectedDrynessLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterlaundrydryercontrols/writeattributeselecteddrynesslevel%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeSelectedDrynessLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterlaundrydryercontrols/writeattributeselecteddrynesslevel%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterlaundrydryercontrols)*