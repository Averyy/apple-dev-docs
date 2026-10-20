# MTRClusterTestCluster

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use MTRClusterUnitTesting

## Declaration

```swift
class MTRClusterTestCluster
```

```objc
@interface MTRClusterTestCluster : MTRClusterUnitTesting
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustertestcluster/init%28device,endpoint,queue%29.md)
### Instance Methods
- [func simpleStructEchoRequest(with: MTRTestClusterClusterSimpleStructEchoRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterSimpleStructResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/simplestructechorequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func test(with: MTRTestClusterClusterTestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustertestcluster/test%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func test(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustertestcluster/test%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testAddArguments(with: MTRTestClusterClusterTestAddArgumentsParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestAddArgumentsResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testaddarguments%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testComplexNullableOptionalRequest(with: MTRTestClusterClusterTestComplexNullableOptionalRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestComplexNullableOptionalResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testcomplexnullableoptionalrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testEmitTestEventRequest(with: MTRTestClusterClusterTestEmitTestEventRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestEmitTestEventResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testemittesteventrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testEmitTestFabricScopedEventRequest(with: MTRTestClusterClusterTestEmitTestFabricScopedEventRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestEmitTestFabricScopedEventResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testemittestfabricscopedeventrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testEnumsRequest(with: MTRTestClusterClusterTestEnumsRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestEnumsResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testenumsrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testListInt8UArgumentRequest(with: MTRTestClusterClusterTestListInt8UArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testlistint8uargumentrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testListInt8UReverseRequest(with: MTRTestClusterClusterTestListInt8UReverseRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestListInt8UReverseResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testlistint8ureverserequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testListNestedStructListArgumentRequest(with: MTRTestClusterClusterTestListNestedStructListArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testlistnestedstructlistargumentrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testListStructArgumentRequest(with: MTRTestClusterClusterTestListStructArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testliststructargumentrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testNestedStructArgumentRequest(with: MTRTestClusterClusterTestNestedStructArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testnestedstructargumentrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testNestedStructListArgumentRequest(with: MTRTestClusterClusterTestNestedStructListArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testnestedstructlistargumentrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testNotHandled(with: MTRTestClusterClusterTestNotHandledParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustertestcluster/testnothandled%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testNotHandled(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustertestcluster/testnothandled%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testNullableOptionalRequest(with: MTRTestClusterClusterTestNullableOptionalRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestNullableOptionalResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testnullableoptionalrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testNullableOptionalRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestNullableOptionalResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testnullableoptionalrequest%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testSimpleArgumentRequest(with: MTRTestClusterClusterTestSimpleArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestSimpleArgumentResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testsimpleargumentrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testSimpleOptionalArgumentRequest(with: MTRTestClusterClusterTestSimpleOptionalArgumentRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustertestcluster/testsimpleoptionalargumentrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testSimpleOptionalArgumentRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustertestcluster/testsimpleoptionalargumentrequest%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testSpecific(with: MTRTestClusterClusterTestSpecificParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestSpecificResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testspecific%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testSpecific(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestSpecificResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/testspecific%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testStructArgumentRequest(with: MTRTestClusterClusterTestStructArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/teststructargumentrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testStructArrayArgumentRequest(with: MTRTestClusterClusterTestStructArrayArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestStructArrayArgumentResponseParams?, (any Error)?) -> Void)](./mtrclustertestcluster/teststructarrayargumentrequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testUnknownCommand(with: MTRTestClusterClusterTestUnknownCommandParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustertestcluster/testunknowncommand%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func testUnknownCommand(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustertestcluster/testunknowncommand%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func timedInvokeRequest(with: MTRTestClusterClusterTimedInvokeRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustertestcluster/timedinvokerequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func timedInvokeRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustertestcluster/timedinvokerequest%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)

## Relationships

### Inherits From
- [MTRClusterUnitTesting](./mtrclusterunittesting.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertestcluster)*