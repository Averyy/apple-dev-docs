# AddMediaIntent

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

An object that describes the user’s request to add media items to their library or to a specific playlist.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object AddMediaIntent
```

## Properties

- `class` (string) *(required)*: The specific type of intent.
- `mediaItems` ([MediaItem]): The media items to add to the user’s library or to a playlist.
- `mediaSearch` (MediaSearch): Parameters that describe the media items to add to the user’s library or to a playlist.
- `mediaDestination` (MediaDestination): The library or playlist to modify.

## Relationships

### Inherits From
- [Intent](intent.md)

## See Also

- [object AddMediaIntentHandlingInvocation](addmediaintenthandlinginvocation.md)
  A request to process an add media intent.
- [type AddMediaIntentHandlingInvocationResponse](addmediaintenthandlinginvocationresponse.md)
  The service’s response to a request to process an add media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediaintent)*