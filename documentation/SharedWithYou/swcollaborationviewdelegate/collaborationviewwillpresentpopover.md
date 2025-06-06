# collaborationViewWillPresentPopover(_:)

**Framework**: Shared With You  
**Kind**: method

Notifies the delegate before the system presents the popover.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func collaborationViewWillPresentPopover(_ collaborationView: SWCollaborationView)
```

## Parameters

- `collaborationView`: The related  .

## See Also

- [func collaborationViewShouldPresentPopover(SWCollaborationView) -> Bool](swcollaborationviewdelegate/collaborationviewshouldpresentpopover(_:).md)
  Asks the delegate whether the system can display the popover.
- [func collaborationViewDidDismissPopover(SWCollaborationView)](swcollaborationviewdelegate/collaborationviewdiddismisspopover(_:).md)
  Notifies the delegate after the system dismisses the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationviewdelegate/collaborationviewwillpresentpopover(_:))*