# load(options:completionHandler:)

**Framework**: StoreKit  
**Kind**: method

Loads the cloud service setup view with the specified options.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func load(options: [SKCloudServiceSetupOptionsKey : Any] = [:]) async throws -> Bool
```

## Mentions

- [Offering Apple Music Subscription in Your App](offering-apple-music-subscription-in-your-app.md)

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func load(options: [SKCloudServiceSetupOptionsKey : Any] = [:]) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `options`: A key that identifies the type of setup the user needs to do. See   for possible values.
- `completionHandler`: An error value that indicates the reason for failure. Possible values are  ,  , and  .

## See Also

- [Offering Apple Music Subscription in Your App](offering-apple-music-subscription-in-your-app.md)
  Allow eligible customers to subscribe to Apple Music.
- [struct SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey.md)
  Keys to specify the types of setup options for a cloud service.
- [class SKArcadeService](skarcadeservice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontroller/load(options:completionhandler:))*