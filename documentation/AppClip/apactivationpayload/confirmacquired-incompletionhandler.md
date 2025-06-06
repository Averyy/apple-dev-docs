# confirmAcquired(in:completionHandler:)

**Framework**: App Clips  
**Kind**: method

Checks whether an App Clip invocation happened at an expected physical location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func confirmAcquired(in region: CLRegion) async throws -> Bool
```

## Mentions

- [Confirming a person’s physical location](confirming-a-person-s-physical-location.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func confirmAcquired(in region: CLRegion) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func confirmAcquired(in region: CLRegion) async throws -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Confirm the user’s location at the time of the App Clip invocation if the App Clip is associated with a physical location. The request to confirm the location fails with [`disallowed`](apactivationpayloaderror/disallowed.md) if the source of the invocation isn’t an NFC tag or visual code.

For the platform to accept the request to confirm the user’s location, you need to make modifications to the `Info.plist` file of the App Clip. For more information, see [`Enabling notifications in App Clips`](enabling-notifications-in-app-clips.md).

> **Note**:  Functionality to confirm the user’s location is only available to App Clips. For the full app, request permission to access the user’s location and make use of the [`Core Location`](https://developer.apple.com/documentation/CoreLocation) framework. For more information, see [`Getting the current location of a device`](https://developer.apple.com/documentation/CoreLocation/getting-the-current-location-of-a-device).

 Functionality to confirm the user’s location is only available to App Clips. For the full app, request permission to access the user’s location and make use of the [`Core Location`](https://developer.apple.com/documentation/CoreLocation) framework. For more information, see [`Getting the current location of a device`](https://developer.apple.com/documentation/CoreLocation/getting-the-current-location-of-a-device).

## Parameters

- `region`: The expected physical location at the time of the App Clip invocation.
- `completionHandler`: This parameter is   if the platform was able to determine the user’s physical location at the time of the App Clip invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/apactivationpayload/confirmacquired(in:completionhandler:))*