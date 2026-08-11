# connect(context:)

**Framework**: Foveated Streaming  
**Kind**: method  
**Required**: Yes

Connect to the provided endpoint.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func connect(context: Self.Context) async throws
```

#### Discussion

This is called when the session begins. Your extension should begin connecting to `context.endpoint` immediately.

> **Note**: If the connection fails.  The error will be presented to the host app.

## Parameters

- `context`: An object used to communicate state back to the host app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingextension/connect(context:))*