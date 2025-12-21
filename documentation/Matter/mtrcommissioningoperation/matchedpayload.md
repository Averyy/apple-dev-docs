# matchedPayload

**Framework**: Matter  
**Kind**: property

If not nil, the payload (from possibly multiple payloads represented by the provided setupPayload) that represents the commissionee we successfully established PASE with.  This will only be non-nil after successful PASE establishment.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
var matchedPayload: MTRSetupPayload? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningoperation/matchedpayload)*