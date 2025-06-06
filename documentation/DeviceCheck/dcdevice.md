# DCDevice

**Framework**: DeviceCheck  
**Kind**: class

A representation of a device that provides a unique, authenticated token.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class DCDevice
```

## Mentions

- [Accessing and modifying per-device data](accessing-and-modifying-per-device-data.md)

#### Overview

Use the shared instance of the `DCDevice` class to generate a token that identifies a device. Call the [`generateToken(completionHandler:)`](dcdevice/generatetoken(completionhandler:).md) method to get the token, and then send it to your server:

```swift
if DCDevice.current.isSupported { // Always test for availability.
    DCDevice.current.generateToken { token, error in
        guard error == nil else { /* Handle the error. */ }

        // Send the token to your server.
    }
}
```

On your server, combine the token with an authentication key that you obtain from Apple, and use the result to request access to two per-device binary digits (bits). After authenticating the device, Apple passes the current values of the bits, along with the date they were last modified, to your server. Your server applies its business logic to this information and communicates the results to your app. For more information about server-side procedures, see [`Accessing and modifying per-device data`](accessing-and-modifying-per-device-data.md).

> **Note**: To use the `DCDevice` class, your app must have an app ID that you register on the [`Apple Developer`](https://developer.apple.comhttps://developer.apple.com/account/) website.

To use the `DCDevice` class, your app must have an app ID that you register on the [`Apple Developer`](https://developer.apple.comhttps://developer.apple.com/account/) website.

Apple records the bits for you, and reports the bits back to you, but you’re responsible for keeping track of what the bits mean. You’re also responsible for determining when to reset the bits for a given device; for example, when a user sells the device to someone else.

## Topics

### Getting the current device
- [class var current: DCDevice](dcdevice/current.md)
  A representation of the device for which you want to query the two bits of data.
### Determining API support
- [var isSupported: Bool](dcdevice/issupported.md)
  A Boolean value that indicates whether the device supports the DeviceCheck API.
### Getting a device token
- [func generateToken(completionHandler: (Data?, (any Error)?) -> Void)](dcdevice/generatetoken(completionhandler:).md)
  Generates a token that identifies the current device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Accessing and modifying per-device data](accessing-and-modifying-per-device-data.md)
  Use a token from your app to query and modify two per-device binary digits stored on an Apple server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcdevice)*