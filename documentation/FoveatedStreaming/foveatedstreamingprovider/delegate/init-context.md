# init(context:)

**Framework**: Foveated Streaming  
**Kind**: init  
**Required**: Yes

Initialize the streaming provider and connect to the provided endpoint.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
init(context: FoveatedStreamingProvider.Context) async throws
```

#### Discussion

This is called when the extension is first loaded. Your extension should begin connecting to `context.endpoint` immediately.

> **Note**: If the connection fails.  The error will be presented to the host app.

## Parameters

- `context`: An object used to communicate state back to the host app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/delegate/init(context:))*