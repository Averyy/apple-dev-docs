# MTRClusterContentLauncher

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
class MTRClusterContentLauncher
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustercontentlauncher/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustercontentlauncher/init(device:endpointid:queue:).md)
### Instance Methods
- [func launchContent(with: MTRContentLauncherClusterLaunchContentParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRContentLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclustercontentlauncher/launchcontent(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func launchContent(with: MTRContentLauncherClusterLaunchContentParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRContentLauncherClusterLaunchResponseParams?, (any Error)?) -> Void)](mtrclustercontentlauncher/launchcontent(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func launchURL(with: MTRContentLauncherClusterLaunchURLParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRContentLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclustercontentlauncher/launchurl(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func launchURL(with: MTRContentLauncherClusterLaunchURLParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRContentLauncherClusterLaunchResponseParams?, (any Error)?) -> Void)](mtrclustercontentlauncher/launchurl(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptHeader(with: MTRReadParams?) -> [String : Any]?](mtrclustercontentlauncher/readattributeacceptheader(with:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustercontentlauncher/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustercontentlauncher/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustercontentlauncher/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustercontentlauncher/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustercontentlauncher/readattributegeneratedcommandlist(with:).md)
- [func readAttributeSupportedStreamingProtocols(with: MTRReadParams?) -> [String : Any]?](mtrclustercontentlauncher/readattributesupportedstreamingprotocols(with:).md)
- [func writeAttributeSupportedStreamingProtocols(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustercontentlauncher/writeattributesupportedstreamingprotocols(withvalue:expectedvalueinterval:).md)
- [func writeAttributeSupportedStreamingProtocols(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustercontentlauncher/writeattributesupportedstreamingprotocols(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustercontentlauncher)*