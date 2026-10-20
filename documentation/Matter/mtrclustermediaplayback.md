# MTRClusterMediaPlayback

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
class MTRClusterMediaPlayback
```

```objc
@interface MTRClusterMediaPlayback : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustermediaplayback/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustermediaplayback/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func fastForward(with: MTRMediaPlaybackClusterFastForwardParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/fastforward%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func fastForward(with: MTRMediaPlaybackClusterFastForwardParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/fastforward%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func fastForward(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/fastforward%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func fastForward(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/fastforward%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func next(with: MTRMediaPlaybackClusterNextParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/next%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func next(with: MTRMediaPlaybackClusterNextParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/next%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func next(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/next%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func next(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/next%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func pause(with: MTRMediaPlaybackClusterPauseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/pause%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func pause(with: MTRMediaPlaybackClusterPauseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/pause%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func pause(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/pause%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func pause(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/pause%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func play(with: MTRMediaPlaybackClusterPlayParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/play%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func play(with: MTRMediaPlaybackClusterPlayParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/play%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func play(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/play%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func play(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/play%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func previous(with: MTRMediaPlaybackClusterPreviousParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/previous%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func previous(with: MTRMediaPlaybackClusterPreviousParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/previous%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func previous(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/previous%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func previous(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/previous%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentState(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributecurrentstate%28with%29.md)
- [func readAttributeDuration(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributeduration%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributePlaybackSpeed(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributeplaybackspeed%28with%29.md)
- [func readAttributeSampledPosition(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributesampledposition%28with%29.md)
- [func readAttributeSeekRangeEnd(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributeseekrangeend%28with%29.md)
- [func readAttributeSeekRangeStart(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributeseekrangestart%28with%29.md)
- [func readAttributeStartTime(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediaplayback/readattributestarttime%28with%29.md)
- [func rewind(with: MTRMediaPlaybackClusterRewindParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/rewind%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func rewind(with: MTRMediaPlaybackClusterRewindParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/rewind%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func rewind(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/rewind%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func rewind(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/rewind%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func seek(with: MTRMediaPlaybackClusterSeekParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/seek%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func seek(with: MTRMediaPlaybackClusterSeekParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/seek%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func skipBackward(with: MTRMediaPlaybackClusterSkipBackwardParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/skipbackward%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func skipBackward(with: MTRMediaPlaybackClusterSkipBackwardParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/skipbackward%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func skipForward(with: MTRMediaPlaybackClusterSkipForwardParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/skipforward%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func skipForward(with: MTRMediaPlaybackClusterSkipForwardParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/skipforward%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func startOver(with: MTRMediaPlaybackClusterStartOverParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/startover%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func startOver(with: MTRMediaPlaybackClusterStartOverParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/startover%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func startOver(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/startover%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func startOver(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/startover%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stop(with: MTRMediaPlaybackClusterStopParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/stop%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stop(with: MTRMediaPlaybackClusterStopPlaybackParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/stop%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/stop%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func stop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](./mtrclustermediaplayback/stop%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func activateAudioTrack(with: MTRMediaPlaybackClusterActivateAudioTrackParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermediaplayback/activateaudiotrack%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func activateTextTrack(with: MTRMediaPlaybackClusterActivateTextTrackParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermediaplayback/activatetexttrack%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func deactivateTextTrack(with: MTRMediaPlaybackClusterDeactivateTextTrackParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermediaplayback/deactivatetexttrack%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func deactivateTextTrack(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermediaplayback/deactivatetexttrack%28withexpectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustermediaplayback)*