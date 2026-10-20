# MTRClusterApplicationLauncher

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
class MTRClusterApplicationLauncher
```

```objc
@interface MTRClusterApplicationLauncher : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterapplicationlauncher/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterapplicationlauncher/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func hideApp(with: MTRApplicationLauncherClusterHideAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclusterapplicationlauncher/hideapp%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func hideApp(with: MTRApplicationLauncherClusterHideAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclusterapplicationlauncher/hideapp%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func hideApp(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclusterapplicationlauncher/hideapp%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func launchApp(with: MTRApplicationLauncherClusterLaunchAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclusterapplicationlauncher/launchapp%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func launchApp(with: MTRApplicationLauncherClusterLaunchAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclusterapplicationlauncher/launchapp%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func launchApp(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclusterapplicationlauncher/launchapp%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationlauncher/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationlauncher/readattributeattributelist%28with%29.md)
- [func readAttributeCatalogList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationlauncher/readattributecataloglist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationlauncher/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentApp(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationlauncher/readattributecurrentapp%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationlauncher/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationlauncher/readattributegeneratedcommandlist%28with%29.md)
- [func stopApp(with: MTRApplicationLauncherClusterStopAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclusterapplicationlauncher/stopapp%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stopApp(with: MTRApplicationLauncherClusterStopAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclusterapplicationlauncher/stopapp%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stopApp(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrclusterapplicationlauncher/stopapp%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func writeAttributeCurrentApp(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterapplicationlauncher/writeattributecurrentapp%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeCurrentApp(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterapplicationlauncher/writeattributecurrentapp%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterapplicationlauncher)*