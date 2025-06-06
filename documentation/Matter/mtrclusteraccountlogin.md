# MTRClusterAccountLogin

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
class MTRClusterAccountLogin
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusteraccountlogin/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusteraccountlogin/init(device:endpointid:queue:).md)
### Instance Methods
- [func getSetupPIN(with: MTRAccountLoginClusterGetSetupPINParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRAccountLoginClusterGetSetupPINResponseParams?, (any Error)?) -> Void)](mtrclusteraccountlogin/getsetuppin(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getSetupPIN(with: MTRAccountLoginClusterGetSetupPINParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRAccountLoginClusterGetSetupPINResponseParams?, (any Error)?) -> Void)](mtrclusteraccountlogin/getsetuppin(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func login(with: MTRAccountLoginClusterLoginParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteraccountlogin/login(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func login(with: MTRAccountLoginClusterLoginParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteraccountlogin/login(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func logout(with: MTRAccountLoginClusterLogoutParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteraccountlogin/logout(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func logout(with: MTRAccountLoginClusterLogoutParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteraccountlogin/logout(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func logout(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusteraccountlogin/logout(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func logout(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusteraccountlogin/logout(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccountlogin/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccountlogin/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccountlogin/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccountlogin/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccountlogin/readattributegeneratedcommandlist(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteraccountlogin)*