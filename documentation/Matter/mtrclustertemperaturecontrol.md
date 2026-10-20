# MTRClusterTemperatureControl

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterTemperatureControl : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustertemperaturecontrol/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeMaxTemperature(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributemaxtemperature%28with%29.md)
- [func readAttributeMinTemperature(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributemintemperature%28with%29.md)
- [func readAttributeSelectedTemperatureLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributeselectedtemperaturelevel%28with%29.md)
- [func readAttributeStep(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributestep%28with%29.md)
- [func readAttributeSupportedTemperatureLevels(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributesupportedtemperaturelevels%28with%29.md)
- [func readAttributeTemperatureSetpoint(with: MTRReadParams?) -> [String : Any]?](./mtrclustertemperaturecontrol/readattributetemperaturesetpoint%28with%29.md)
- [func setTemperatureWith(MTRTemperatureControlClusterSetTemperatureParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustertemperaturecontrol/settemperaturewith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setTemperatureWithExpectedValues([[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustertemperaturecontrol/settemperaturewithexpectedvalues%28_,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertemperaturecontrol)*