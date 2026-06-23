# enableCredentialSharingMode(withExtendedPANId:completion:)

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
func enableCredentialSharingModeWithExtendedPANId(extendedPANId xpanId: Data) async throws
```

#### Discussion

This method scans for Thread credential sharing capable Apple Border Routers, selects an eligible device, and requests to generate an ephemeral 9-digit code and start credential sharing mode.

When you call this method, an alert appears asking for user permission to access credentials. The one-time admin code is displayed internally via an alert; it is not returned to the caller.

/// - Parameters:

- extendedPANID: The extended PAN identifier of the Thread network.
- completion: The completion handler the framework calls after the user acknowledges the alert. The `error` parameter is nil on success, or non-nil if credential sharing mode could not be enabled.

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declarations: ```swift
// Completion handler form:
func enableCredentialSharingModeWithExtendedPANId(extendedPANId: Data, completion: @escaping (Error?) -> Void)

// Async form (throws on failure):
func enableCredentialSharingModeWithExtendedPANId(extendedPANId: Data) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient/enablecredentialsharingmode(withextendedpanid:completion:))*