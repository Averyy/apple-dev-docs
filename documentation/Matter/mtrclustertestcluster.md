# MTRClusterTestCluster

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
class MTRClusterTestCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustertestcluster/init(device:endpoint:queue:).md)
### Instance Methods
- [func simpleStructEchoRequest(with: MTRTestClusterClusterSimpleStructEchoRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterSimpleStructResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/simplestructechorequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func test(with: MTRTestClusterClusterTestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustertestcluster/test(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func test(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustertestcluster/test(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testAddArguments(with: MTRTestClusterClusterTestAddArgumentsParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestAddArgumentsResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testaddarguments(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testComplexNullableOptionalRequest(with: MTRTestClusterClusterTestComplexNullableOptionalRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestComplexNullableOptionalResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testcomplexnullableoptionalrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testEmitTestEventRequest(with: MTRTestClusterClusterTestEmitTestEventRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestEmitTestEventResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testemittesteventrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testEmitTestFabricScopedEventRequest(with: MTRTestClusterClusterTestEmitTestFabricScopedEventRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestEmitTestFabricScopedEventResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testemittestfabricscopedeventrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testEnumsRequest(with: MTRTestClusterClusterTestEnumsRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestEnumsResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testenumsrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testListInt8UArgumentRequest(with: MTRTestClusterClusterTestListInt8UArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testlistint8uargumentrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testListInt8UReverseRequest(with: MTRTestClusterClusterTestListInt8UReverseRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestListInt8UReverseResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testlistint8ureverserequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testListNestedStructListArgumentRequest(with: MTRTestClusterClusterTestListNestedStructListArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testlistnestedstructlistargumentrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testListStructArgumentRequest(with: MTRTestClusterClusterTestListStructArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testliststructargumentrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testNestedStructArgumentRequest(with: MTRTestClusterClusterTestNestedStructArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testnestedstructargumentrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testNestedStructListArgumentRequest(with: MTRTestClusterClusterTestNestedStructListArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testnestedstructlistargumentrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testNotHandled(with: MTRTestClusterClusterTestNotHandledParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustertestcluster/testnothandled(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testNotHandled(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustertestcluster/testnothandled(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testNullableOptionalRequest(with: MTRTestClusterClusterTestNullableOptionalRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestNullableOptionalResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testnullableoptionalrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testNullableOptionalRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestNullableOptionalResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testnullableoptionalrequest(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testSimpleArgumentRequest(with: MTRTestClusterClusterTestSimpleArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestSimpleArgumentResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testsimpleargumentrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testSimpleOptionalArgumentRequest(with: MTRTestClusterClusterTestSimpleOptionalArgumentRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustertestcluster/testsimpleoptionalargumentrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testSimpleOptionalArgumentRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustertestcluster/testsimpleoptionalargumentrequest(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testSpecific(with: MTRTestClusterClusterTestSpecificParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestSpecificResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testspecific(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testSpecific(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestSpecificResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/testspecific(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testStructArgumentRequest(with: MTRTestClusterClusterTestStructArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/teststructargumentrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testStructArrayArgumentRequest(with: MTRTestClusterClusterTestStructArrayArgumentRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTestClusterClusterTestStructArrayArgumentResponseParams?, (any Error)?) -> Void)](mtrclustertestcluster/teststructarrayargumentrequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testUnknownCommand(with: MTRTestClusterClusterTestUnknownCommandParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustertestcluster/testunknowncommand(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func testUnknownCommand(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustertestcluster/testunknowncommand(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func timedInvokeRequest(with: MTRTestClusterClusterTimedInvokeRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustertestcluster/timedinvokerequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func timedInvokeRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustertestcluster/timedinvokerequest(withexpectedvalues:expectedvalueinterval:completionhandler:).md)

## Relationships

### Inherits From
- [MTRClusterUnitTesting](mtrclusterunittesting.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertestcluster)*