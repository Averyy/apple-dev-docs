# match(for:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Creates a match from an invitation that the local player accepts.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func match(for invite: GKInvite) async throws -> GKMatch
```

#### Discussion

Use this method when you implement your own interface to inform you when the local player joins a match.

## Parameters

- `invite`: The invitation that the local player accepts.
- `completionHandler`: The block that GameKit calls when it completes the request. This block receives the following parameters: - **`match`**: The match that GameKit creates when the local player accepts the invitation. If unsuccessful, this parameter is `nil`.
- **`error`**: Describes an error if one occurs, or `nil` if the operation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/match(for:completionhandler:))*