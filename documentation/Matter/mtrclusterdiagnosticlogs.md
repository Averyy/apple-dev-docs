# MTRClusterDiagnosticLogs

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
class MTRClusterDiagnosticLogs
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterdiagnosticlogs/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterdiagnosticlogs/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdiagnosticlogs/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdiagnosticlogs/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterdiagnosticlogs/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterdiagnosticlogs/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdiagnosticlogs/readattributegeneratedcommandlist(with:).md)
- [func retrieveLogsRequest(with: MTRDiagnosticLogsClusterRetrieveLogsRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDiagnosticLogsClusterRetrieveLogsResponseParams?, (any Error)?) -> Void)](mtrclusterdiagnosticlogs/retrievelogsrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func retrieveLogsRequest(with: MTRDiagnosticLogsClusterRetrieveLogsRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDiagnosticLogsClusterRetrieveLogsResponseParams?, (any Error)?) -> Void)](mtrclusterdiagnosticlogs/retrievelogsrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdiagnosticlogs)*