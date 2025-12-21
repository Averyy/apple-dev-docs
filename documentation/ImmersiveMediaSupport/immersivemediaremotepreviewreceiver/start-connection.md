# start(connection:)

**Framework**: Immersive Media Support  
**Kind**: method

Performs the necessary steps to start receiving remote Immersive video frames using the given network connection.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func start(connection: NWConnection) async throws
```

#### Discussion

> **Note**: This function throws if anything fails establishing the connection.

## Parameters

- `connection`: The network connection to use for communication and receive remote frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewreceiver/start(connection:))*