# loadReceivedChallenges(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Loads the list of outstanding challenges.

**Availability**:
- iOS 6.0+ - Deprecated in 26.0
- iPadOS 6.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
class func loadReceivedChallenges(completionHandler: (@Sendable ([GKChallenge]?, (any Error)?) -> Void)? = nil)
```

```swift
class func loadReceivedChallenges() async throws -> [GKChallenge]
```

```objc
+ (void) loadReceivedChallengesWithCompletionHandler:(void (^)(NSArray<GKChallenge *> *challenges, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameters:

  - **`challenges`**: The challenges the local player issued.
  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallenge/loadreceivedchallenges(completionhandler:))*