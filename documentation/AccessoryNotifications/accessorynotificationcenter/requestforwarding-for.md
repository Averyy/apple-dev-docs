# requestForwarding(for:)

**Framework**: Accessory Notifications  
**Kind**: method

Requests permission to forward notifications to the specified accessory.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func requestForwarding(for accessory: ASAccessory) async throws -> ForwardingDecision
```

#### Discussion

This method prompts the person to select which apps on their device can forward notifications to your accessory. The person can choose all apps, some apps, no apps, or dismiss the prompt. This method throws [`AccessoryError.unsupportedPlatform`](accessoryerror/unsupportedplatform.md) if called on an unsupported device; notification forwarding supports iPhone only.

## Parameters

- `accessory`: An accessory object that [`AccessorySetupKit`](https://developer.apple.comhttps://developer.apple.com/documentation/accessorysetupkit) provides when your companion app registers the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter/requestforwarding(for:))*