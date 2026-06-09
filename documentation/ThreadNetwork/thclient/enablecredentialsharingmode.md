# enableCredentialSharingMode(_:)

**Framework**: ThreadNetwork  
**Kind**: method

Triggers Credential Share mode on a nearby eligible Apple Border Router (tvOS(27.0)).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 13.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
func enableCredentialSharingMode() async throws -> String
```

#### Discussion

This method scans for Thread credential sharing capable Apple Border Routers, selects an eligible device, and requests to generate an ephemeral 9-digit code and start credential sharing mode.

When you call this method, an alert appears asking for user permission to access credentials.

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declarations: ```swift
// Completion handler form:
func enableCredentialSharingMode(completionHandler: @escaping (String?, Error?) -> Void)

// Async form:
func enableCredentialSharingMode() async throws -> String
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completion`: The completion handler the framework calls when the one-time admin code becomes available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/enablecredentialsharingmode(_:))*