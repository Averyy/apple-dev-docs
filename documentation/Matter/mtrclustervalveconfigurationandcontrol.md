# MTRClusterValveConfigurationAndControl

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
class MTRClusterValveConfigurationAndControl
```

```objc
@interface MTRClusterValveConfigurationAndControl : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustervalveconfigurationandcontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func close(with: MTRValveConfigurationAndControlClusterCloseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustervalveconfigurationandcontrol/close%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func close(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustervalveconfigurationandcontrol/close%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func open(with: MTRValveConfigurationAndControlClusterOpenParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustervalveconfigurationandcontrol/open%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func open(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustervalveconfigurationandcontrol/open%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributeattributelist%28with%29.md)
- [func readAttributeAutoCloseTime(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributeautoclosetime%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributecurrentlevel%28with%29.md)
- [func readAttributeCurrentState(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributecurrentstate%28with%29.md)
- [func readAttributeDefaultOpenDuration(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributedefaultopenduration%28with%29.md)
- [func readAttributeDefaultOpenLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributedefaultopenlevel%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeLevelStep(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributelevelstep%28with%29.md)
- [func readAttributeOpenDuration(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributeopenduration%28with%29.md)
- [func readAttributeRemainingDuration(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributeremainingduration%28with%29.md)
- [func readAttributeTargetLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributetargetlevel%28with%29.md)
- [func readAttributeTargetState(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributetargetstate%28with%29.md)
- [func readAttributeValveFault(with: MTRReadParams?) -> [String : Any]?](./mtrclustervalveconfigurationandcontrol/readattributevalvefault%28with%29.md)
- [func writeAttributeDefaultOpenDuration(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustervalveconfigurationandcontrol/writeattributedefaultopenduration%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeDefaultOpenDuration(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustervalveconfigurationandcontrol/writeattributedefaultopenduration%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeDefaultOpenLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustervalveconfigurationandcontrol/writeattributedefaultopenlevel%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeDefaultOpenLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustervalveconfigurationandcontrol/writeattributedefaultopenlevel%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustervalveconfigurationandcontrol)*