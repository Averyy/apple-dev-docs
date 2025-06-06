# isSpatial

**Framework**: Group Activities  
**Kind**: property

A Boolean value that indicates whether the person supports being in a shared simulation space for an activity.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
let isSpatial: Bool
```

## Mentions

- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Discussion

The value of this property is `true` when the current person supports activities that place participants relative to the activity itself. The person must use a device that supports spatial experiences, and must configure their spatial Persona to support inclusion in a shared simulation space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstate/isspatial)*