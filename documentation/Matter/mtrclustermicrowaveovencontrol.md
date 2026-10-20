# MTRClusterMicrowaveOvenControl

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterMicrowaveOvenControl : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustermicrowaveovencontrol/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func addMoreTime(with: MTRMicrowaveOvenControlClusterAddMoreTimeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermicrowaveovencontrol/addmoretime%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributeclusterrevision%28with%29.md)
- [func readAttributeCookTime(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributecooktime%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeMaxCookTime(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributemaxcooktime%28with%29.md)
- [func readAttributeMaxPower(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributemaxpower%28with%29.md)
- [func readAttributeMinPower(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributeminpower%28with%29.md)
- [func readAttributePowerSetting(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributepowersetting%28with%29.md)
- [func readAttributePowerStep(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributepowerstep%28with%29.md)
- [func readAttributeWattRating(with: MTRReadParams?) -> [String : Any]?](./mtrclustermicrowaveovencontrol/readattributewattrating%28with%29.md)
- [func setCookingParametersWith(MTRMicrowaveOvenControlClusterSetCookingParametersParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermicrowaveovencontrol/setcookingparameterswith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setCookingParametersWithExpectedValues([[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermicrowaveovencontrol/setcookingparameterswithexpectedvalues%28_,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustermicrowaveovencontrol)*