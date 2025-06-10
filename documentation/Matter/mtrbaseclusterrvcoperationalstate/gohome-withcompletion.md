# goHome(with:completion:)

**Framework**: Matter  
**Kind**: method

Command GoHome

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
func goHome(with params: MTRRVCOperationalStateClusterGoHomeParams?) async throws -> MTRRVCOperationalStateClusterOperationalCommandResponseParams
```

#### Discussion

On receipt of this command, the device SHALL start seeking the charging dock, if possible in the current state of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterrvcoperationalstate/gohome(with:completion:))*