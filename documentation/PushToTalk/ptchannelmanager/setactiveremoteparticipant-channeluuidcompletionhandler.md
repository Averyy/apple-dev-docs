# setActiveRemoteParticipant(_:channelUUID:completionHandler:)

**Framework**: Push to Talk  
**Kind**: method

Sets the active remote participant with the channel identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func setActiveRemoteParticipant(_ participant: PTParticipant?, channelUUID: UUID) async throws
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setActiveRemoteParticipant(_ participant: PTParticipant?, channelUUID: UUID) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func setActiveRemoteParticipant(_ participant: PTParticipant?, channelUUID: UUID) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

When you receive incoming audio from a remote participant, set the participant value, which updates the system user interface and blocks transmission by the local user. When the user stops speaking, set the active participant to `nil`.

## Parameters

- `participant`: The remote participant to become active.
- `channelUUID`: The channel identifier the participant becomes active in.
- `completionHandler`: The completion handler that contains an optional error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/setactiveremoteparticipant(_:channeluuid:completionhandler:))*