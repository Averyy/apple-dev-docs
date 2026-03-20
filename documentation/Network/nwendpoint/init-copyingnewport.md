# init(copying:newPort:)

**Framework**: Network  
**Kind**: init

Creates a new `NWEndpoint` by copying an existing endpoint and specifying a new port.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
init?(copying endpoint: NWEndpoint, newPort: NWEndpoint.Port)
```

#### Return Value

A new `NWEndpoint` instance copied from the source endpoint with a new port, or `nil` if the original endpoint is invalid or if modifying the port for the copy results in an invalid endpoint. Examples of invalid endpoints are malformed IP addresses or port numbers greater than 65535.

## Parameters

- `endpoint`: The source endpoint to copy.
- `newPort`: The new port to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/init(copying:newport:))*