# MTRClusterMediaPlayback

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
class MTRClusterMediaPlayback
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustermediaplayback/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustermediaplayback/init(device:endpointid:queue:).md)
### Instance Methods
- [func fastForward(with: MTRMediaPlaybackClusterFastForwardParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/fastforward(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func fastForward(with: MTRMediaPlaybackClusterFastForwardParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/fastforward(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func fastForward(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/fastforward(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func fastForward(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/fastforward(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func next(with: MTRMediaPlaybackClusterNextParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/next(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func next(with: MTRMediaPlaybackClusterNextParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/next(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func next(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/next(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func next(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/next(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func pause(with: MTRMediaPlaybackClusterPauseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/pause(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func pause(with: MTRMediaPlaybackClusterPauseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/pause(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func pause(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/pause(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func pause(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/pause(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func play(with: MTRMediaPlaybackClusterPlayParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/play(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func play(with: MTRMediaPlaybackClusterPlayParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/play(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func play(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/play(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func play(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/play(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func previous(with: MTRMediaPlaybackClusterPreviousParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/previous(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func previous(with: MTRMediaPlaybackClusterPreviousParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/previous(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func previous(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/previous(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func previous(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/previous(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentState(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributecurrentstate(with:).md)
- [func readAttributeDuration(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributeduration(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributegeneratedcommandlist(with:).md)
- [func readAttributePlaybackSpeed(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributeplaybackspeed(with:).md)
- [func readAttributeSampledPosition(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributesampledposition(with:).md)
- [func readAttributeSeekRangeEnd(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributeseekrangeend(with:).md)
- [func readAttributeSeekRangeStart(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributeseekrangestart(with:).md)
- [func readAttributeStartTime(with: MTRReadParams?) -> [String : Any]?](mtrclustermediaplayback/readattributestarttime(with:).md)
- [func rewind(with: MTRMediaPlaybackClusterRewindParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/rewind(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func rewind(with: MTRMediaPlaybackClusterRewindParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/rewind(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func rewind(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/rewind(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func rewind(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/rewind(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func seek(with: MTRMediaPlaybackClusterSeekParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/seek(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func seek(with: MTRMediaPlaybackClusterSeekParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/seek(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func skipBackward(with: MTRMediaPlaybackClusterSkipBackwardParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/skipbackward(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func skipBackward(with: MTRMediaPlaybackClusterSkipBackwardParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/skipbackward(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func skipForward(with: MTRMediaPlaybackClusterSkipForwardParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/skipforward(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func skipForward(with: MTRMediaPlaybackClusterSkipForwardParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/skipforward(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func startOver(with: MTRMediaPlaybackClusterStartOverParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/startover(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func startOver(with: MTRMediaPlaybackClusterStartOverParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/startover(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func startOver(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/startover(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func startOver(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/startover(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stop(with: MTRMediaPlaybackClusterStopParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/stop(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stop(with: MTRMediaPlaybackClusterStopPlaybackParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/stop(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/stop(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func stop(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRMediaPlaybackClusterPlaybackResponseParams?, (any Error)?) -> Void)](mtrclustermediaplayback/stop(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func activateAudioTrack(with: MTRMediaPlaybackClusterActivateAudioTrackParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermediaplayback/activateaudiotrack(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func activateTextTrack(with: MTRMediaPlaybackClusterActivateTextTrackParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermediaplayback/activatetexttrack(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func deactivateTextTrack(with: MTRMediaPlaybackClusterDeactivateTextTrackParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermediaplayback/deactivatetexttrack(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func deactivateTextTrack(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermediaplayback/deactivatetexttrack(withexpectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustermediaplayback)*