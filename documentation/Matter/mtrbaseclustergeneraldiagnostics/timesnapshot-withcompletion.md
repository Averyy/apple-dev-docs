# timeSnapshot(with:completion:)

**Framework**: Matter  
**Kind**: method

Command TimeSnapshot

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
func timeSnapshot(with params: MTRGeneralDiagnosticsClusterTimeSnapshotParams?) async throws -> MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams
```

#### Discussion

This command MAY be used by a client to obtain a correlated view of both System Time, and, if currently synchronized and supported, “wall clock time” of the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergeneraldiagnostics/timesnapshot(with:completion:))*