# init(networkParameters:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a preview sender using the specified network parameters, if any.

**Availability**:
- macOS 26.0+

## Declaration

```swift
init(networkParameters: NWParameters? = nil) async throws
```

#### Discussion

> **Note**: This function throws if anything fails during initialization.

## Parameters

- `networkParameters`: The network parameters to use when connecting to receivers (optional).


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/init(networkparameters:))*