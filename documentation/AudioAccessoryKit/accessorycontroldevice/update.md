# update(_:)

**Framework**: AudioAccessoryKit  
**Kind**: method

Updates the accessory’s configuration.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
final nonisolated(nonsending) func update(_ configuration: AccessoryControlDevice.Configuration) async throws
```

#### Discussion

> ❗ **Important**: Call this method only from your app extension.

For example, the following code updates device placement:

```swift
// Get the current state.
let accessoryDevice = try AccessoryControlDevice.current(for: myAccessory)

// Modify the configuration with new values.
var configuration = accessoryDevice.configuration
configuration.devicePlacement = .onHead

// Apply the updated configuration.
try await accessoryDevice.update(configuration)
print("Successfully updated device configuration")
```

Always register a capability before trying to update it. For example, the code above is valid only if you included the [`placement`](accessorycontroldevice/capabilities/placement.md) capability when registering the accessory.

This method throws an error if the update fails.

## Parameters

- `configuration`: The new configuration to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/update(_:))*