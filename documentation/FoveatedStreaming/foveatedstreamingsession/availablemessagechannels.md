# availableMessageChannels

**Framework**: Foveated Streaming  
**Kind**: property

A list of all available message channels in this session.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
@MainActor
final var availableMessageChannels: Set<FoveatedStreamingSession.MessageChannel.ID> { get }
```

#### Discussion

Observe this property to know when the endpoint creates a new message channel. Message channels can only be initialized by the endpoint.

For example, you can observe the available message channels by employing [`withObservationTracking(_:onChange:)`](https://developer.apple.com/documentation/Observation/withObservationTracking(_:onChange:)).

```swift
@MainActor
private func monitorAvailableChannels() {
    withObservationTracking {
        for channelId in session.availableMessageChannels {
            // Get the message channel.
        }
    } onChange: {
        Task { @MainActor in
            self.monitorAvailableChannels()
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/availablemessagechannels)*