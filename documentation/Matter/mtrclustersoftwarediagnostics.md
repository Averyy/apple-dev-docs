# MTRClusterSoftwareDiagnostics

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
class MTRClusterSoftwareDiagnostics
```

```objc
@interface MTRClusterSoftwareDiagnostics : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustersoftwarediagnostics/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustersoftwarediagnostics/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustersoftwarediagnostics/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustersoftwarediagnostics/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustersoftwarediagnostics/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentHeapFree(with: MTRReadParams?) -> [String : Any]?](./mtrclustersoftwarediagnostics/readattributecurrentheapfree%28with%29.md)
- [func readAttributeCurrentHeapHighWatermark(with: MTRReadParams?) -> [String : Any]?](./mtrclustersoftwarediagnostics/readattributecurrentheaphighwatermark%28with%29.md)
- [func readAttributeCurrentHeapUsed(with: MTRReadParams?) -> [String : Any]?](./mtrclustersoftwarediagnostics/readattributecurrentheapused%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustersoftwarediagnostics/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustersoftwarediagnostics/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeThreadMetrics(with: MTRReadParams?) -> [String : Any]?](./mtrclustersoftwarediagnostics/readattributethreadmetrics%28with%29.md)
- [func resetWatermarks(with: MTRSoftwareDiagnosticsClusterResetWatermarksParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustersoftwarediagnostics/resetwatermarks%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func resetWatermarks(with: MTRSoftwareDiagnosticsClusterResetWatermarksParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustersoftwarediagnostics/resetwatermarks%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func resetWatermarks(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustersoftwarediagnostics/resetwatermarks%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func resetWatermarks(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustersoftwarediagnostics/resetwatermarks%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustersoftwarediagnostics)*