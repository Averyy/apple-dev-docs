# MTRClusterChannel

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterChannel : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterchannel/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterchannel/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func change(with: MTRChannelClusterChangeChannelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRChannelClusterChangeChannelResponseParams?, (any Error)?) -> Void)](./mtrclusterchannel/change%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func change(with: MTRChannelClusterChangeChannelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRChannelClusterChangeChannelResponseParams?, (any Error)?) -> Void)](./mtrclusterchannel/change%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func changeByNumber(with: MTRChannelClusterChangeChannelByNumberParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterchannel/changebynumber%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func changeByNumber(with: MTRChannelClusterChangeChannelByNumberParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterchannel/changebynumber%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterchannel/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterchannel/readattributeattributelist%28with%29.md)
- [func readAttributeChannelList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterchannel/readattributechannellist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterchannel/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentChannel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterchannel/readattributecurrentchannel%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterchannel/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterchannel/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeLineup(with: MTRReadParams?) -> [String : Any]?](./mtrclusterchannel/readattributelineup%28with%29.md)
- [func skip(with: MTRChannelClusterSkipChannelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterchannel/skip%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func skip(with: MTRChannelClusterSkipChannelParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterchannel/skip%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func cancelRecordProgram(with: MTRChannelClusterCancelRecordProgramParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterchannel/cancelrecordprogram%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getProgramGuide(with: MTRChannelClusterGetProgramGuideParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRChannelClusterProgramGuideResponseParams?, (any Error)?) -> Void)](./mtrclusterchannel/getprogramguide%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getProgramGuide(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRChannelClusterProgramGuideResponseParams?, (any Error)?) -> Void)](./mtrclusterchannel/getprogramguide%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func recordProgram(with: MTRChannelClusterRecordProgramParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterchannel/recordprogram%28with,expectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterchannel)*