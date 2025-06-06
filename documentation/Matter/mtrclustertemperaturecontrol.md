# MTRClusterTemperatureControl

**Framework**: Matter  
**Kind**: class

Cluster Temperature Control Attributes and commands for configuring the temperature control, and reporting temperature.

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
class MTRClusterTemperatureControl
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustertemperaturecontrol/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributegeneratedcommandlist(with:).md)
- [func readAttributeMaxTemperature(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributemaxtemperature(with:).md)
- [func readAttributeMinTemperature(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributemintemperature(with:).md)
- [func readAttributeSelectedTemperatureLevel(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributeselectedtemperaturelevel(with:).md)
- [func readAttributeStep(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributestep(with:).md)
- [func readAttributeSupportedTemperatureLevels(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributesupportedtemperaturelevels(with:).md)
- [func readAttributeTemperatureSetpoint(with: MTRReadParams?) -> [String : Any]?](mtrclustertemperaturecontrol/readattributetemperaturesetpoint(with:).md)
- [func setTemperatureWith(MTRTemperatureControlClusterSetTemperatureParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustertemperaturecontrol/settemperaturewith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setTemperatureWithExpectedValues([[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustertemperaturecontrol/settemperaturewithexpectedvalues(_:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertemperaturecontrol)*