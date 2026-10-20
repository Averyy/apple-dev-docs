# MTRClusterAccountLogin

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
class MTRClusterAccountLogin
```

```objc
@interface MTRClusterAccountLogin : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusteraccountlogin/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusteraccountlogin/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func getSetupPIN(with: MTRAccountLoginClusterGetSetupPINParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRAccountLoginClusterGetSetupPINResponseParams?, (any Error)?) -> Void)](./mtrclusteraccountlogin/getsetuppin%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getSetupPIN(with: MTRAccountLoginClusterGetSetupPINParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRAccountLoginClusterGetSetupPINResponseParams?, (any Error)?) -> Void)](./mtrclusteraccountlogin/getsetuppin%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func login(with: MTRAccountLoginClusterLoginParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteraccountlogin/login%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func login(with: MTRAccountLoginClusterLoginParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteraccountlogin/login%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func logout(with: MTRAccountLoginClusterLogoutParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteraccountlogin/logout%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func logout(with: MTRAccountLoginClusterLogoutParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteraccountlogin/logout%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func logout(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteraccountlogin/logout%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func logout(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteraccountlogin/logout%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccountlogin/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccountlogin/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccountlogin/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccountlogin/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccountlogin/readattributegeneratedcommandlist%28with%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteraccountlogin)*