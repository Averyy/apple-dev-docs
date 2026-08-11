# FoveatedStreamingExtension

**Framework**: Foveated Streaming  
**Kind**: protocol

A foveated streaming provider extension.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol FoveatedStreamingExtension : AnyObject, AppExtension
```

#### Overview

Foveated streaming providers are a system extension that allows developers to use your custom protocol with a [`FoveatedStreamingSession`](foveatedstreamingsession.md).

Foveated streaming providers require the `com.apple.developer.foveated-streaming-provider` entitlement.

```swift
@main
final class MyStreamingProvider: FoveatedStreamingExtension {
    func connect(context: Context) async throws { /* ... */ }
    func disconnect() async throws { /* ... */ }
    func openMessageChannel(_ channel: MessageChannel) throws { /* ... */ }
    var immersiveScene: some View { /* ... */ }
}
```

## Topics

### Associated Types
- [associatedtype Content : View](foveatedstreamingextension/content.md)
  The type of the view that renders the streamed content.
### Instance Properties
- [var immersiveScene: Self.Content](foveatedstreamingextension/immersivescene.md)
  The SwiftUI view that renders the streamed content.
### Instance Methods
- [func connect(context: Self.Context) async throws](foveatedstreamingextension/connect(context:).md)
  Connect to the provided endpoint.
- [func disconnect() async throws](foveatedstreamingextension/disconnect.md)
  Disconnect from the streaming endpoint.
- [func openMessageChannel(Self.MessageChannel) throws](foveatedstreamingextension/openmessagechannel(_:).md)
  Handles a message channel opened by the host app.
### Type Aliases
- [FoveatedStreamingExtension.Context](foveatedstreamingextension/context.md)
  The context object provided to the extension when it connects.
- [FoveatedStreamingExtension.Endpoint](foveatedstreamingextension/endpoint.md)
  The streaming endpoint the extension connects to.
- [FoveatedStreamingExtension.FocusRegion](foveatedstreamingextension/focusregion.md)
  The approximate region where the person is looking.
- [FoveatedStreamingExtension.MessageChannel](foveatedstreamingextension/messagechannel.md)
  A message channel between the host app and the extension.
- [FoveatedStreamingExtension.Status](foveatedstreamingextension/status.md)
  The lifecycle state of the extension.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingextension)*