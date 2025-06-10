# MTRClusterTimeSynchronization

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustertimesynchronization/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributeclusterrevision(with:).md)
- [func readAttributeDSTOffset(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributedstoffset(with:).md)
- [func readAttributeDSTOffsetListMaxSize(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributedstoffsetlistmaxsize(with:).md)
- [func readAttributeDefaultNTP(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributedefaultntp(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributegeneratedcommandlist(with:).md)
- [func readAttributeGranularity(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributegranularity(with:).md)
- [func readAttributeLocalTime(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributelocaltime(with:).md)
- [func readAttributeNTPServerAvailable(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributentpserveravailable(with:).md)
- [func readAttributeSupportsDNSResolve(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributesupportsdnsresolve(with:).md)
- [func readAttributeTimeSource(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributetimesource(with:).md)
- [func readAttributeTimeZone(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributetimezone(with:).md)
- [func readAttributeTimeZoneDatabase(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributetimezonedatabase(with:).md)
- [func readAttributeTimeZoneListMaxSize(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributetimezonelistmaxsize(with:).md)
- [func readAttributeTrustedTimeSource(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributetrustedtimesource(with:).md)
- [func readAttributeUTCTime(with: MTRReadParams?) -> [String : Any]?](mtrclustertimesynchronization/readattributeutctime(with:).md)
- [func setDSTOffsetWith(MTRTimeSynchronizationClusterSetDSTOffsetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustertimesynchronization/setdstoffsetwith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setDefaultNTPWith(MTRTimeSynchronizationClusterSetDefaultNTPParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustertimesynchronization/setdefaultntpwith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setTimeZoneWith(MTRTimeSynchronizationClusterSetTimeZoneParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRTimeSynchronizationClusterSetTimeZoneResponseParams?, (any Error)?) -> Void)](mtrclustertimesynchronization/settimezonewith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setTrustedTimeSourceWith(MTRTimeSynchronizationClusterSetTrustedTimeSourceParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustertimesynchronization/settrustedtimesourcewith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setUTCTimeWith(MTRTimeSynchronizationClusterSetUTCTimeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustertimesynchronization/setutctimewith(_:expectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertimesynchronization)*