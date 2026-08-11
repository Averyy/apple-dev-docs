# retrieveActiveCredentialsForNearbyNetworks(completion:)

**Framework**: ThreadNetwork  
**Kind**: method

Requests all active Thread credentials with active border routers around from the framework.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 13.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
var activeCredentialsForNearbyNetworks: Set<THCredentials> { get async throws }
```

#### Discussion

When calling this method, you will receive credentials for active border routers around. You receive all credentials agnostic to team ID. Unlike [`retrieveAllActiveCredentials(_:)`](thclient/retrieveallactivecredentials(_:).md), this method returns active credentials on the device regardless of who actually stored it.

> **Note**: This method asks for user permission to share available credentials. If user denies the permission then the completion will contain error with code 15.

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
var activeCredentialsForNearbyNetworks: Set<THCredentials> { get async throws }
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completion`: The completion handler the framework calls when the credentials become available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/retrieveactivecredentialsfornearbynetworks(completion:))*