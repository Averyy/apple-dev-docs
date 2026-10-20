# stopReports(withController:nodeId:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func stopReports(withController controller: Any?, nodeId: UInt64, completion: @escaping @Sendable () -> Void)
```

```swift
func stopReports(withController controller: Any?, nodeId: UInt64) async
```

```objc
- (void) stopReportsWithController:(id) controller nodeId:(uint64_t) nodeId completion:(dispatch_block_t) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/stopreports(withcontroller:nodeid:completion:))*