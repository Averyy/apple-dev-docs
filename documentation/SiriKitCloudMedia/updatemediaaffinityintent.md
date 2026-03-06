# UpdateMediaAffinityIntent

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

An object that describes a user’s stated preference regarding media items.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object UpdateMediaAffinityIntent
```

## Properties

- `class` (string) *(required)*: The specific type of intent.
- `affinityType` (MediaAffinityType): The user’s preference for the media items.
- `mediaItems` ([MediaItem]): Specific media items the user expresses a preference for.
- `mediaSearch` (MediaSearch): The description of the media items the user expresses a preference for.

## Relationships

### Inherits From
- [Intent](intent.md)

## See Also

- [object UpdateMediaAffinityIntentHandlingInvocation](updatemediaaffinityintenthandlinginvocation.md)
  A request to process an update media affinity intent.
- [type UpdateMediaAffinityIntentHandlingInvocationResponse](updatemediaaffinityintenthandlinginvocationresponse.md)
  The service’s response to a request to process an update media affinity intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinityintent)*