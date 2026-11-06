# configuration

**Framework**: Foveated Streaming  
**Kind**: property  
**Role**: Instance Property

The connection parameters the host app supplied, keyed by name.

**Availability**:
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
final var configuration: [String : FoveatedStreamingSession.ConfigurationValue] { get }
```

## Discussion

The host app passes these to [`connect(endpoint:streamingProvider:configuration:)`](../foveatedstreamingsession/connect%28endpoint,streamingprovider,configuration%29.md). The framework doesn’t interpret them — document the keys and values your provider accepts, and read them here when you connect:

```swift
func connect(context: Context) async throws {
    if case .int(let bitrate) = context.configuration["maxBitrate"] {
        // Apply the requested bitrate.
    }
}
```

Empty if the host app connected without supplying parameters. Apply your own defaults for any key that’s absent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext/configuration)*