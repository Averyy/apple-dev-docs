# bottomBar

**Framework**: StoreKit  
**Kind**: property

A placement that locates the subscription controls in a bar near the bottom of the main scroll view in a subscription store view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static var bottomBar: SubscriptionStoreControlPlacementKey { get }
```

#### Discussion

The bottom bar conditonally applies a special visual treatment when it overlaps the main content of the subscription store view. The content within the bottom bar doesn’t scroll with the rest of the content in the main scroll view.

## See Also

- [static var bottom: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/bottom.md)
  A placement that anchors the subscription controls to the bottom edge of the view.
- [static var leading: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/leading.md)
  A placement that anchors the subscription controls to the leading edge of the view.
- [static var scrollView: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/scrollview.md)
  A placement that locates the subscription controls within the main scroll view of a subscription store view.
- [static var trailing: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/trailing.md)
  A placement that anchors the subscription controls to the trailing edge of the view.
- [static var buttonsInBottomBar: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/buttonsinbottombar.md)
  A hybrid placement that positions subscription controls within the main scroll view, and places auxiliary buttons in the bottom bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolplacementkey/bottombar)*