# init(position:direction:role:)

**Framework**: Group Activities  
**Kind**: init

Creates a seat element with the specified position, direction, and role information.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(position: SpatialTemplateElementPosition, direction: SpatialTemplateElementDirection = .lookingAt(.app), role: (any SpatialTemplateRole)? = nil)
```

#### Return Value

An initialized seat element for you to add to a custom spatial template.

## Parameters

- `position`: The position of this seat in the shared coordinate   space. Place seats relative to your app’s content, which is at   the origin of the coordinate space.
- `direction`: The initial direction for the participant to face.   Specify a value to point the person in the direction of another   participant or a specific location in the coordinate space. If you   don’t specify this parameter, the participant faces the app’s content.
- `role`: The custom role you assign to the seat. Roles are an optional   way to place spatial Personas in an immersive space. For example,   you might define roles for two opposing teams in a game and use   those roles to place the participants relative to   the game content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateseatelement/init(position:direction:role:))*