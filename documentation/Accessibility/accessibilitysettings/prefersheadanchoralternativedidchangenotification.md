# prefersHeadAnchorAlternativeDidChangeNotification

**Framework**: Accessibility  
**Kind**: property

A notification that posts when the system setting for head-anchored content changes.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static var prefersHeadAnchorAlternativeDidChangeNotification: Notification.Name { get }
```

#### Discussion

The system sends this notification when the setting for head-anchored content changes. When you receive this notification, call [`prefersHeadAnchorAlternative`](accessibilitysettings/prefersheadanchoralternative.md) to get the new setting.

On Apple Vision Pro, apps can create a heads-up display effect by setting up content to follow the person’s head position. This effect allows the content to remain in the same position, no matter where the person looks. However, some assistive technologies are incompatible with this type of content. For example, a technology might use the person’s head movements to control the current selection, or they might magnify content to make it easier to read. Anchoring content to the head position prevents these technologies from interacting with that content.

## See Also

- [static var prefersHeadAnchorAlternative: Bool](accessibilitysettings/prefersheadanchoralternative.md)
  A Boolean value that indicates the person’s preference for content that follows their head position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/prefersheadanchoralternativedidchangenotification)*