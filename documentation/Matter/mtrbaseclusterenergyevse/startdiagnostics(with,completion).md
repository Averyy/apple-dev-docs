# startDiagnostics(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command StartDiagnostics

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
func startDiagnostics(with params: MTREnergyEVSEClusterStartDiagnosticsParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func startDiagnostics(with params: MTREnergyEVSEClusterStartDiagnosticsParams?) async throws
```

```objc
- (void) startDiagnosticsWithParams:(MTREnergyEVSEClusterStartDiagnosticsParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

Allows a client to put the EVSE into a self-diagnostics mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterenergyevse/startdiagnostics(with:completion:))*