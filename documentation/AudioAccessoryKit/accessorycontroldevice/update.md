# update(_:)

**Framework**: AudioAccessoryKit  
**Kind**: method

Updates the accessory’s configuration.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func update(_ configuration: AccessoryControlDevice.Configuration) async throws
```

#### Discussion

For example, the following code updates device placement:

```swift
// Get the current state.
let accessoryDevice = try AccessoryControlDevice.current(myAccessory)

// Modify the configuration with new values.
var configuration = accessoryDevice.configuration
configuration.devicePlacement = .onHead

// Apply the updated configuration.
try await accessoryDevice.update(configuration)
print("Successfully updated device configuration")
```

This method throws an error if the update fails.

## Parameters

- `configuration`: The new configuration to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/update(_:))*