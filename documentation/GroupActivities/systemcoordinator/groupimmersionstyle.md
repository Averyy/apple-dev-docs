# groupImmersionStyle

**Framework**: Group Activities  
**Kind**: property

The presentation style to apply to an immersive space for the current activity.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final var groupImmersionStyle: SystemCoordinator.GroupImmersionStyles { get }
```

## Mentions

- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Discussion

During an activity, the system uses this property to communicate the style for a currently open immersive space. When no participants are displaying an immersive space, the value of this property is `nil`. When any participant displays a space, the system sets the value for all participants to the immersion style of the newly presented space. When a participant presents a space with a different presentation style, the system also updates the property to reflect the new style. For example, if the group is currently in a space with the [`full`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/full) style, it updates the property when someone presents a space with the [`full`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/full) style.

Use this property to synchronize the level of immersion for all participants. Keeping the participants at the same level of immersion preserves the shared context of your activity. When the value of the property changes, transition the current participant to the new immersion level only if doing so doesn’t disrupt any other ongoing tasks. For example, if the current person is editing content in an unrelated window, don’t transition them automatically. Instead, give them the choice of when to make the transition.

## See Also

- [SystemCoordinator.GroupImmersionStyles](systemcoordinator/groupimmersionstyles.md)
  An asynchronous sequence that contains one or more incoming immersion styles for you to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/groupimmersionstyle)*