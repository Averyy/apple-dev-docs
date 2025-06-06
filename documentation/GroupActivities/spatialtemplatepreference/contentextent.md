# contentExtent(_:)

**Framework**: Group Activities  
**Kind**: method

Sets the distance between the app’s content and any participants.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func contentExtent(_ contentExtent: CGFloat) -> SpatialTemplatePreference
```

## Mentions

- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Discussion

Use this modifier to set the distance between your app’s content and the participants in a shared context. You might use this modifier if the intrinsic size of your content doesn’t represent an optimal viewing distance. Specify the new size in points.

If you don’t apply this modifier, the system uses the intrinsic size of the scene’s content to determine the viewing distance for participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplatepreference/contentextent(_:))*