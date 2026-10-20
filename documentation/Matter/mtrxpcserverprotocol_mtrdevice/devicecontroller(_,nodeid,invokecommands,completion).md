# deviceController(_:nodeID:invokeCommands:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
optional func deviceController(_ controller: UUID, nodeID: NSNumber, invokeCommands commands: [[MTRCommandWithRequiredResponse]], completion: @escaping @Sendable ([[String : Any]]?, (any Error)?) -> Void)
```

```swift
optional func deviceController(_ controller: UUID, nodeID: NSNumber, invokeCommands commands: [[MTRCommandWithRequiredResponse]]) async throws -> [[String : Any]]
```

```objc
- (void) deviceController:(NSUUID *) controller nodeID:(NSNumber *) nodeID invokeCommands:(NSArray<NSArray<MTRCommandWithRequiredResponse *> *> *) commands completion:(MTRDeviceResponseHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:invokecommands:completion:))*