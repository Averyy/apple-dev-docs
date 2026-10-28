# expensivePathsProhibited(_:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Prohibit using expensive paths.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func expensivePathsProhibited(_ prohibited: Bool) -> Self
```

## Discussion

Prohibit connections and listeners from using a network interface that is considered expensive by the system, for example some cellular interfaces.

## Parameters

- `prohibited`: True if expensive paths are prohibited, false otherwise.

## Default Implementations

### NWParametersProvider Implementations
- [func expensivePathsProhibited(Bool) -> Self](./expensivepathsprohibited%28_%29-53yp0.md)
  Prohibit using expensive paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/expensivepathsprohibited(_:))*