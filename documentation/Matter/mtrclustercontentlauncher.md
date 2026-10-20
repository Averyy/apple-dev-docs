# MTRClusterContentLauncher

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
class MTRClusterContentLauncher
```

```objc
@interface MTRClusterContentLauncher : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustercontentlauncher/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustercontentlauncher/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func launchContent(with: MTRContentLauncherClusterLaunchContentParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRContentLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclustercontentlauncher/launchcontent%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func launchContent(with: MTRContentLauncherClusterLaunchContentParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRContentLauncherClusterLaunchResponseParams?, (any Error)?) -> Void)](./mtrclustercontentlauncher/launchcontent%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func launchURL(with: MTRContentLauncherClusterLaunchURLParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRContentLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclustercontentlauncher/launchurl%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func launchURL(with: MTRContentLauncherClusterLaunchURLParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRContentLauncherClusterLaunchResponseParams?, (any Error)?) -> Void)](./mtrclustercontentlauncher/launchurl%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptHeader(with: MTRReadParams?) -> [String : Any]?](./mtrclustercontentlauncher/readattributeacceptheader%28with%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustercontentlauncher/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustercontentlauncher/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustercontentlauncher/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustercontentlauncher/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustercontentlauncher/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeSupportedStreamingProtocols(with: MTRReadParams?) -> [String : Any]?](./mtrclustercontentlauncher/readattributesupportedstreamingprotocols%28with%29.md)
- [func writeAttributeSupportedStreamingProtocols(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercontentlauncher/writeattributesupportedstreamingprotocols%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeSupportedStreamingProtocols(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercontentlauncher/writeattributesupportedstreamingprotocols%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustercontentlauncher)*