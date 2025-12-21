# associationKind

**Framework**: Group Activities  
**Kind**: property

An optional value that indicates the kind of group activity association, if any.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@MainActor
var associationKind: GroupActivityAssociationKind? { get set }
```

#### Discussion

Set this property to `nil` to remove the view’s association with the current SharePlay group activity.

You should create an interaction for each view that your app will associate and then enable and disable them as needed. If multiple views with active associations are found, the most recently associated interaction will be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivityassociationinteraction/associationkind)*