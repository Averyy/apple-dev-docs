# invokeCommand(withEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func invokeCommand(withEndpointID endpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: [String : Any]?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, queue: dispatch_queue_t, completion: @escaping @Sendable ([[String : Any]]?, (any Error)?) -> Void)
```

```swift
func invokeCommand(withEndpointID endpointID: NSNumber, clusterID: NSNumber, commandID: NSNumber, commandFields: [String : Any]?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, queue: dispatch_queue_t) async throws -> [[String : Any]]
```

```objc
- (void) invokeCommandWithEndpointID:(NSNumber *) endpointID clusterID:(NSNumber *) clusterID commandID:(NSNumber *) commandID commandFields:(NSDictionary<NSString *,id> *) commandFields expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedValues expectedValueInterval:(NSNumber *) expectedValueInterval queue:(dispatch_queue_t) queue completion:(MTRDeviceResponseHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/invokecommand(withendpointid:clusterid:commandid:commandfields:expectedvalues:expectedvalueinterval:queue:completion:))*