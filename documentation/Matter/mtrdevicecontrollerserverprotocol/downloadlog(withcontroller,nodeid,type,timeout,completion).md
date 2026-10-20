# downloadLog(withController:nodeId:type:timeout:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
optional func downloadLog(withController controller: Any?, nodeId: NSNumber, type: MTRDiagnosticLogType, timeout: TimeInterval, completion: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```swift
optional func downloadLog(withController controller: Any?, nodeId: NSNumber, type: MTRDiagnosticLogType, timeout: TimeInterval) async throws -> String
```

```objc
- (void) downloadLogWithController:(id) controller nodeId:(NSNumber *) nodeId type:(MTRDiagnosticLogType) type timeout:(NSTimeInterval) timeout completion:(void (^)(NSString *url, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/downloadlog(withcontroller:nodeid:type:timeout:completion:))*