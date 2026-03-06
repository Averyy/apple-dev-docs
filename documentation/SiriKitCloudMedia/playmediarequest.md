# PlayMediaRequest

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A request for a media playback queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayMediaRequest
```

## Properties

- `constraints` (Constraints) *(required)*: Limitations on the type and quantity of content the client can receive.
- `userActivity` (UserActivity) *(required)*: A description of the playback queue. Your service provides the [`UserActivity`](useractivity.md) after it successfully handles a play media intent.
- `version` (string) *(required)*: The version of the `SiriKitMediaAPI` library the client uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediarequest)*