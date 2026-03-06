# Activities

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents an activity curator.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Activities
```

## Topics

### Related Objects
- [object Activities.Attributes](activities/attributes-data.dictionary.md)
  The attributes for an activities resource.
- [object Activities.Relationships](activities/relationships-data.dictionary.md)
  The relationships for an activity resource.

## Properties

- `id` (string) *(required)*: The identifier for the activity.
- `type` (string) *(required)*: This value must always be `activities`.
- `href` (string) *(required)*: The relative location for the activity resource.
- `attributes` (Activities.Attributes): The attributes for the activity.
- `relationships` (Activities.Relationships): The relationships for the activity.

## See Also

- [object ActivitiesResponse](activitiesresponse.md)
  The response to a request for activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/activities)*