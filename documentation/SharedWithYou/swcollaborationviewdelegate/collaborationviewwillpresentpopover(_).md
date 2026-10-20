# collaborationViewWillPresentPopover(_:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) collaborationViewWillPresentPopover:(SWCollaborationView *) collaborationView;
```

## Parameters

- `collaborationView`: The related `SWCollaborationView`.

## See Also

### Responding to popover activity
- [func collaborationViewShouldPresentPopover(SWCollaborationView) -> Bool](./collaborationviewshouldpresentpopover%28_%29.md)
  Asks the delegate whether the system can display the popover.
- [func collaborationViewDidDismissPopover(SWCollaborationView)](./collaborationviewdiddismisspopover%28_%29.md)
  Notifies the delegate after the system dismisses the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationviewdelegate/collaborationviewwillpresentpopover(_:))*