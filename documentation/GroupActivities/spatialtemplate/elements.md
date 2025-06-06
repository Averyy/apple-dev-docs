# elements

**Framework**: Group Activities  
**Kind**: property  
**Required**: Yes

The collection of spatial Persona seats this template contains.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var elements: [any SpatialTemplateElement] { get }
```

#### Discussion

This property contains the seat locations for the participants. Add the seats your template requires, and specify each seat’s location relative to your app’s shared scene. For each seat, you can also specify the direction that seat faces, and optional role information. The system fills seats in the same order they appear in the array.

To place the current participant in a seat with a specific role, use the [`SystemCoordinator`](systemcoordinator.md) object to assign that role to the participant. The system assigns the first available seat with that role to the participant. If a seat with the requested role is unavailable, the system assigns the participant to the next available seat without a role.

You can specify as many seats as you want in this property, even if there aren’t enough participants to fill all of the seats. If some seats in your template have roles, include enough additional seats without roles to accommodate all participants initially.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplate/elements)*