# deviceController(_:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func deviceController(_ controller: UUID, nodeID: NSNumber, invokeCommandWithEndpointID endpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, timedInvokeTimeout timeout: NSNumber?, serverSideProcessingTimeout: NSNumber?, completion: @escaping @Sendable ([[String : Any]]?, (any Error)?) -> Void)
```

```swift
func deviceController(_ controller: UUID, nodeID: NSNumber, invokeCommandWithEndpointID endpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: Any, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, timedInvokeTimeout timeout: NSNumber?, serverSideProcessingTimeout: NSNumber?) async throws -> [[String : Any]]
```

```objc
- (void) deviceController:(NSUUID *) controller nodeID:(NSNumber *) nodeID invokeCommandWithEndpointID:(NSNumber *) endpointID clusterID:(NSNumber *) clusterID commandID:(NSNumber *) commandID commandFields:(id) commandFields expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedValues expectedValueInterval:(NSNumber *) expectedValueInterval timedInvokeTimeout:(NSNumber *) timeout serverSideProcessingTimeout:(NSNumber *) serverSideProcessingTimeout completion:(MTRDeviceResponseHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:invokecommandwithendpointid:clusterid:commandid:commandfields:expectedvalues:expectedvalueinterval:timedinvoketimeout:serversideprocessingtimeout:completion:))*