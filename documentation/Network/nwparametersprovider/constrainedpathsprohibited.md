# constrainedPathsProhibited(_:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

Prohibit using constrained paths.

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
func constrainedPathsProhibited(_ prohibited: Bool) -> Self
```

#### Discussion

Prohibit connections and listeners from using a network interface that is considered constrained by the system, for example an interface in Low Data Mode.

## Parameters

- `prohibited`: True if constrained paths are prohibited, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/constrainedpathsprohibited(_:))*