# performAccessorySetup(using:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Performs the process of setting up accessories with Apple Home.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+

## Declaration

```swift
func performAccessorySetup(using request: HMAccessorySetupRequest) async throws -> HMAccessorySetupResult
```

#### Discussion

During the setup process, the framework adds each accessory to a home, assigns it to a room, and provides further configuration based on its services.

## Parameters

- `request`: The accessory setup request.
- `completion`: A block that the framework invokes once the setup process completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetupmanager/performaccessorysetup(using:completionhandler:))*