# MTRClusterChannel

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRClusterChannel
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterchannel/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterchannel/init(device:endpointid:queue:).md)
### Instance Methods
- [func change(with: MTRChannelClusterChangeChannelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRChannelClusterChangeChannelResponseParams?, (any Error)?) -> Void)](mtrclusterchannel/change(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func change(with: MTRChannelClusterChangeChannelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRChannelClusterChangeChannelResponseParams?, (any Error)?) -> Void)](mtrclusterchannel/change(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func changeByNumber(with: MTRChannelClusterChangeChannelByNumberParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterchannel/changebynumber(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func changeByNumber(with: MTRChannelClusterChangeChannelByNumberParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusterchannel/changebynumber(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterchannel/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterchannel/readattributeattributelist(with:).md)
- [func readAttributeChannelList(with: MTRReadParams?) -> [String : Any]?](mtrclusterchannel/readattributechannellist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterchannel/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentChannel(with: MTRReadParams?) -> [String : Any]?](mtrclusterchannel/readattributecurrentchannel(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterchannel/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterchannel/readattributegeneratedcommandlist(with:).md)
- [func readAttributeLineup(with: MTRReadParams?) -> [String : Any]?](mtrclusterchannel/readattributelineup(with:).md)
- [func skip(with: MTRChannelClusterSkipChannelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterchannel/skip(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func skip(with: MTRChannelClusterSkipChannelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusterchannel/skip(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func cancelRecordProgram(with: MTRChannelClusterCancelRecordProgramParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterchannel/cancelrecordprogram(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getProgramGuide(with: MTRChannelClusterGetProgramGuideParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRChannelClusterProgramGuideResponseParams?, (any Error)?) -> Void)](mtrclusterchannel/getprogramguide(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getProgramGuide(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRChannelClusterProgramGuideResponseParams?, (any Error)?) -> Void)](mtrclusterchannel/getprogramguide(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func recordProgram(with: MTRChannelClusterRecordProgramParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterchannel/recordprogram(with:expectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterchannel)*