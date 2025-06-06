# MTRClusterApplicationLauncher

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
class MTRClusterApplicationLauncher
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterapplicationlauncher/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterapplicationlauncher/init(device:endpointid:queue:).md)
### Instance Methods
- [func hideApp(with: MTRApplicationLauncherClusterHideAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclusterapplicationlauncher/hideapp(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func hideApp(with: MTRApplicationLauncherClusterHideAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclusterapplicationlauncher/hideapp(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func hideApp(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclusterapplicationlauncher/hideapp(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func launchApp(with: MTRApplicationLauncherClusterLaunchAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclusterapplicationlauncher/launchapp(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func launchApp(with: MTRApplicationLauncherClusterLaunchAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclusterapplicationlauncher/launchapp(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func launchApp(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclusterapplicationlauncher/launchapp(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterapplicationlauncher/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterapplicationlauncher/readattributeattributelist(with:).md)
- [func readAttributeCatalogList(with: MTRReadParams?) -> [String : Any]?](mtrclusterapplicationlauncher/readattributecataloglist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterapplicationlauncher/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentApp(with: MTRReadParams?) -> [String : Any]?](mtrclusterapplicationlauncher/readattributecurrentapp(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterapplicationlauncher/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterapplicationlauncher/readattributegeneratedcommandlist(with:).md)
- [func stopApp(with: MTRApplicationLauncherClusterStopAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclusterapplicationlauncher/stopapp(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stopApp(with: MTRApplicationLauncherClusterStopAppParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclusterapplicationlauncher/stopapp(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stopApp(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrclusterapplicationlauncher/stopapp(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func writeAttributeCurrentApp(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterapplicationlauncher/writeattributecurrentapp(withvalue:expectedvalueinterval:).md)
- [func writeAttributeCurrentApp(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterapplicationlauncher/writeattributecurrentapp(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterapplicationlauncher)*