# MTRClusterSoftwareDiagnostics

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
class MTRClusterSoftwareDiagnostics
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustersoftwarediagnostics/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustersoftwarediagnostics/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustersoftwarediagnostics/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustersoftwarediagnostics/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustersoftwarediagnostics/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentHeapFree(with: MTRReadParams?) -> [String : Any]?](mtrclustersoftwarediagnostics/readattributecurrentheapfree(with:).md)
- [func readAttributeCurrentHeapHighWatermark(with: MTRReadParams?) -> [String : Any]?](mtrclustersoftwarediagnostics/readattributecurrentheaphighwatermark(with:).md)
- [func readAttributeCurrentHeapUsed(with: MTRReadParams?) -> [String : Any]?](mtrclustersoftwarediagnostics/readattributecurrentheapused(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustersoftwarediagnostics/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustersoftwarediagnostics/readattributegeneratedcommandlist(with:).md)
- [func readAttributeThreadMetrics(with: MTRReadParams?) -> [String : Any]?](mtrclustersoftwarediagnostics/readattributethreadmetrics(with:).md)
- [func resetWatermarks(with: MTRSoftwareDiagnosticsClusterResetWatermarksParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustersoftwarediagnostics/resetwatermarks(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func resetWatermarks(with: MTRSoftwareDiagnosticsClusterResetWatermarksParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustersoftwarediagnostics/resetwatermarks(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func resetWatermarks(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustersoftwarediagnostics/resetwatermarks(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func resetWatermarks(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustersoftwarediagnostics/resetwatermarks(withexpectedvalues:expectedvalueinterval:completionhandler:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustersoftwarediagnostics)*