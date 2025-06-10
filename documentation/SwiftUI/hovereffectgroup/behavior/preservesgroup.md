# preservesGroup

**Framework**: SwiftUI  
**Kind**: property

Preserves the current phase of the group.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static let preservesGroup: HoverEffectGroup.Behavior
```

#### Discussion

Use this behavior when an effect should not activate other effects in a group, unless the group already active. This is useful for describing which parts of a view should trigger an effect, while allowing other areas to simply prevent the effect from ending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectgroup/behavior/preservesgroup)*