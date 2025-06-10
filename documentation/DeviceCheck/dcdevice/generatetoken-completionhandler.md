# generateToken(completionHandler:)

**Framework**: DeviceCheck  
**Kind**: method

Generates a token that identifies the current device.

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
func generateToken() async throws -> Data
```

#### Discussion

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func generateToken() async throws -> Data
``` For example: ```swift
let token = try await generateToken()
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Your server uses the generated token in its requests to get or set the persistent bits for the current device. You should treat the token you receive in the completion block as single-use. Although the token remains valid long enough for your server to retry a specific request if necessary, you should not use a token multiple times. Instead, use this method to generate a new token.

> **Note**: The app you use to generate the token must be associated with your developer account; otherwise, the generation request fails.

## Parameters

- `completion`: A completion block that includes the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcdevice/generatetoken(completionhandler:))*