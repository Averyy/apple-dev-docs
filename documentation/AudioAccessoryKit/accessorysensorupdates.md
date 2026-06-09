# AccessorySensorUpdates

**Framework**: AudioAccessoryKit  
**Kind**: struct

Subscribes to a stream of raw sensor data packets from a connected accessory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct AccessorySensorUpdates
```

#### Overview

An Audio Rendering Extension launched by AudioToolbox uses this type to receive sensor data from a 3P accessory that has registered `.headTracking` via `AccessoryControlDevice`. Data is brokered through `audioaccessoryd` over XPC.

No XPC resources are acquired until iteration begins. Cancel the owning `Task` to stop receiving updates and release the connection.

#### Usage

```swift
guard AccessorySensorUpdates.isSupported else { return }
let updates = AccessorySensorUpdates(for: accessoryIdentifier)
sensorTask = Task { [weak self] in
    do {
        for try await update in updates {
            switch update {
            case .packet(let data):
                self?.processSensorData(data)
            case .malformedPacket:
                // Non-terminal; stream continues with subsequent packets
                break
            }
        }
    } catch AccessorySensorUpdates.StreamError.connectionLost {
        // Terminal; stream is over
    }
}
```

## Topics

### Initializers
- [init(for: String)](accessorysensorupdates/init(for:).md)
  Creates a sensor update sequence for the specified accessory.
### Type Properties
- [static var isSupported: Bool](accessorysensorupdates/issupported.md)
  Returns `true` when the running OS version supports `AccessorySensorUpdates`.
### Enumerations
- [AccessorySensorUpdates.StreamError](accessorysensorupdates/streamerror.md)
- [AccessorySensorUpdates.Update](accessorysensorupdates/update.md)
  A single update emitted by the stream.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorysensorupdates)*