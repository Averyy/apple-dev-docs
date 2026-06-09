# payloadTestRequest(with:completion:)

**Framework**: Matter  
**Kind**: method

Command PayloadTestRequest

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
func payloadTestRequest(with params: MTRGeneralDiagnosticsClusterPayloadTestRequestParams) async throws -> MTRGeneralDiagnosticsClusterPayloadTestResponseParams
```

#### Discussion

This command provides a means for certification tests or manufacturer’s internal tests to validate particular command handling and encoding constraints by generating a response of a given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergeneraldiagnostics/payloadtestrequest(with:completion:))*