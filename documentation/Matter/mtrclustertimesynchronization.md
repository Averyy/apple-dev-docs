# MTRClusterTimeSynchronization

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Time Synchronization Accurate time is required for a number of reasons, including scheduling, display and validating security materials.

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
class MTRClusterTimeSynchronization
```

```objc
@interface MTRClusterTimeSynchronization : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustertimesynchronization/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributeclusterrevision%28with%29.md)
- [func readAttributeDSTOffset(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributedstoffset%28with%29.md)
- [func readAttributeDSTOffsetListMaxSize(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributedstoffsetlistmaxsize%28with%29.md)
- [func readAttributeDefaultNTP(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributedefaultntp%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeGranularity(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributegranularity%28with%29.md)
- [func readAttributeLocalTime(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributelocaltime%28with%29.md)
- [func readAttributeNTPServerAvailable(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributentpserveravailable%28with%29.md)
- [func readAttributeSupportsDNSResolve(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributesupportsdnsresolve%28with%29.md)
- [func readAttributeTimeSource(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributetimesource%28with%29.md)
- [func readAttributeTimeZone(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributetimezone%28with%29.md)
- [func readAttributeTimeZoneDatabase(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributetimezonedatabase%28with%29.md)
- [func readAttributeTimeZoneListMaxSize(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributetimezonelistmaxsize%28with%29.md)
- [func readAttributeTrustedTimeSource(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributetrustedtimesource%28with%29.md)
- [func readAttributeUTCTime(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimesynchronization/readattributeutctime%28with%29.md)
- [func setDSTOffsetWith(MTRTimeSynchronizationClusterSetDSTOffsetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustertimesynchronization/setdstoffsetwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setDefaultNTPWith(MTRTimeSynchronizationClusterSetDefaultNTPParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustertimesynchronization/setdefaultntpwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setTimeZoneWith(MTRTimeSynchronizationClusterSetTimeZoneParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRTimeSynchronizationClusterSetTimeZoneResponseParams?, (any Error)?) -> Void)](./mtrclustertimesynchronization/settimezonewith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setTrustedTimeSourceWith(MTRTimeSynchronizationClusterSetTrustedTimeSourceParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustertimesynchronization/settrustedtimesourcewith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setUTCTimeWith(MTRTimeSynchronizationClusterSetUTCTimeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustertimesynchronization/setutctimewith%28_,expectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertimesynchronization)*