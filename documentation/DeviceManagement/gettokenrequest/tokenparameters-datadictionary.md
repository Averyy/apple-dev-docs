# GetTokenRequest.TokenParameters

**Framework**: Device Management  
**Kind**: dictionary

Parameters that the system uses to generate the token.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
object GetTokenRequest.TokenParameters
```

## Properties

- `PhoneUDID` (string): The identifier of the phone paired to the watch. The `com.apple.watch.pairing` service type requires this key. Available: iOS 17+ | iPadOS 17+
- `SecurityToken` (string): A security token to generate the server token. The `com.apple.watch.pairing` service type requires this key. Available: iOS 17+ | iPadOS 17+
- `WatchUDID` (string): The identifier of the watch paired to the phone. The `com.apple.watch.pairing` service type requires this key. Available: iOS 17+ | iPadOS 17+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/gettokenrequest/tokenparameters-data.dictionary)*