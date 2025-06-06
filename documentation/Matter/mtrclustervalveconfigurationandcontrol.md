# MTRClusterValveConfigurationAndControl

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
class MTRClusterValveConfigurationAndControl
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustervalveconfigurationandcontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func close(with: MTRValveConfigurationAndControlClusterCloseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustervalveconfigurationandcontrol/close(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func close(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustervalveconfigurationandcontrol/close(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func open(with: MTRValveConfigurationAndControlClusterOpenParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustervalveconfigurationandcontrol/open(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func open(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustervalveconfigurationandcontrol/open(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributeattributelist(with:).md)
- [func readAttributeAutoCloseTime(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributeautoclosetime(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentLevel(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributecurrentlevel(with:).md)
- [func readAttributeCurrentState(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributecurrentstate(with:).md)
- [func readAttributeDefaultOpenDuration(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributedefaultopenduration(with:).md)
- [func readAttributeDefaultOpenLevel(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributedefaultopenlevel(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributegeneratedcommandlist(with:).md)
- [func readAttributeLevelStep(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributelevelstep(with:).md)
- [func readAttributeOpenDuration(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributeopenduration(with:).md)
- [func readAttributeRemainingDuration(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributeremainingduration(with:).md)
- [func readAttributeTargetLevel(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributetargetlevel(with:).md)
- [func readAttributeTargetState(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributetargetstate(with:).md)
- [func readAttributeValveFault(with: MTRReadParams?) -> [String : Any]?](mtrclustervalveconfigurationandcontrol/readattributevalvefault(with:).md)
- [func writeAttributeDefaultOpenDuration(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustervalveconfigurationandcontrol/writeattributedefaultopenduration(withvalue:expectedvalueinterval:).md)
- [func writeAttributeDefaultOpenDuration(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustervalveconfigurationandcontrol/writeattributedefaultopenduration(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeDefaultOpenLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustervalveconfigurationandcontrol/writeattributedefaultopenlevel(withvalue:expectedvalueinterval:).md)
- [func writeAttributeDefaultOpenLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustervalveconfigurationandcontrol/writeattributedefaultopenlevel(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustervalveconfigurationandcontrol)*