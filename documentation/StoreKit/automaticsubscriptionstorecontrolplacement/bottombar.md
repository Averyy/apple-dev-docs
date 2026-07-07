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
static var bottomBar: AutomaticSubscriptionStoreControlPlacement { get }
```

#### Discussion

The bottom bar conditonally applies a special visual treatment when it overlaps the main content of the subscription store view. The content within the bottom bar doesn’t scroll with the rest of the content in the main scroll view.

## See Also

- [static var automatic: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/automatic.md)
  A context-appropriate placement that the system determines automatically.
- [static var buttonsInBottomBar: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/buttonsinbottombar.md)
  A hybrid placement that positions subscription controls within the main scroll view, and places auxiliary buttons in the bottom bar.
- [static var scrollView: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/scrollview.md)
  A placement that locates the subscription controls within the main scroll view of a subscription store view.
- [static var bottom: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/bottom.md)
  A placement that anchors the subscription controls to the bottom edge of the view.
- [static var leading: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/leading.md)
  A placement that anchors the subscription controls to the leading edge of the view.
- [static var trailing: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/trailing.md)
  A placement that anchors the subscription controls to the trailing edge of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/automaticsubscriptionstorecontrolplacement/bottombar)*