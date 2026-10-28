# collaborationViewShouldPresentPopover(_:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the system can display the popover.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func collaborationViewShouldPresentPopover(_ collaborationView: SWCollaborationView) -> Bool
```

```objc
- (BOOL) collaborationViewShouldPresentPopover:(SWCollaborationView *) collaborationView;
```

## Return Value

`true` if the system should present the popover; otherwise `false`.

## Parameters

- `collaborationView`: The related `SWCollaborationView`.

## See Also

### Responding to popover activity
- [func collaborationViewDidDismissPopover(SWCollaborationView)](./collaborationviewdiddismisspopover%28_%29.md)
  Notifies the delegate after the system dismisses the popover.
- [func collaborationViewWillPresentPopover(SWCollaborationView)](./collaborationviewwillpresentpopover%28_%29.md)
  Notifies the delegate before the system presents the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationviewdelegate/collaborationviewshouldpresentpopover(_:))*