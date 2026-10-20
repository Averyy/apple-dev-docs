# downloadLog(of:nodeID:timeout:completion:)

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
func downloadLog(of type: MTRDiagnosticLogType, nodeID: NSNumber, timeout: TimeInterval, completion: @escaping @Sendable (URL?, (any Error)?) -> Void)
```

```swift
func downloadLog(of type: MTRDiagnosticLogType, nodeID: NSNumber, timeout: TimeInterval) async throws -> URL
```

```objc
- (void) downloadLogOfType:(MTRDiagnosticLogType) type nodeID:(NSNumber *) nodeID timeout:(NSTimeInterval) timeout completion:(void (^)(NSURL *url, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevice/downloadlog(of:nodeid:timeout:completion:))*