# MTRClusterMicrowaveOvenControl

**Framework**: Matter  
**Kind**: class

Cluster Microwave Oven Control Attributes and commands for configuring the microwave oven control, and reporting cooking stats.

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
class MTRClusterMicrowaveOvenControl
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustermicrowaveovencontrol/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func addMoreTime(with: MTRMicrowaveOvenControlClusterAddMoreTimeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermicrowaveovencontrol/addmoretime(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributeclusterrevision(with:).md)
- [func readAttributeCookTime(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributecooktime(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributegeneratedcommandlist(with:).md)
- [func readAttributeMaxCookTime(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributemaxcooktime(with:).md)
- [func readAttributeMaxPower(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributemaxpower(with:).md)
- [func readAttributeMinPower(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributeminpower(with:).md)
- [func readAttributePowerSetting(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributepowersetting(with:).md)
- [func readAttributePowerStep(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributepowerstep(with:).md)
- [func readAttributeWattRating(with: MTRReadParams?) -> [String : Any]?](mtrclustermicrowaveovencontrol/readattributewattrating(with:).md)
- [func setCookingParametersWith(MTRMicrowaveOvenControlClusterSetCookingParametersParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermicrowaveovencontrol/setcookingparameterswith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setCookingParametersWithExpectedValues([[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermicrowaveovencontrol/setcookingparameterswithexpectedvalues(_:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustermicrowaveovencontrol)*