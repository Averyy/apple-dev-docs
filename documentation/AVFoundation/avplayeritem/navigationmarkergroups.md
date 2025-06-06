# navigationMarkerGroups

**Framework**: AVFoundation  
**Kind**: property

The time marker groups that provide ways to navigate the player item’s content.

**Availability**:
- tvOS ?+

## Declaration

```swift
@MainActor
var navigationMarkerGroups: [AVNavigationMarkersGroup] { get set }
```

#### Discussion

A navigation marker group provides a set of time markers for navigating playback. The most common form of navigation marker group is a chapter list; however, you can also provide other sets of markers to allow a user to jump to significant events in the presentation. For example, a “Goals Scored” marker group might summarize key moments in a recorded sporting event. When you present a player item containing marker groups with the [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) class, the user interface provides options for navigating each group.

To provide a chapter list, use the first item in the [`navigationMarkerGroups`](avplayeritem/navigationmarkergroups.md) array and set its title property to `nil`. To provide additional or alternate means of navigating content, use a unique title value for each navigation marker group in the array.

## See Also

- [var nextContentProposal: AVContentProposal?](avplayeritem/nextcontentproposal.md)
  The item proposed to follow the current content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/navigationmarkergroups)*