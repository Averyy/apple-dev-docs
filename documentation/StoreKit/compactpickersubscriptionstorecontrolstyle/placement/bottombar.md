# bottomBar

**Framework**: StoreKit  
**Kind**: property

A placement that locates the compact picker in a bar near the bottom of the main scroll view in a subscription store view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static var bottomBar: CompactPickerSubscriptionStoreControlStyle.Placement { get }
```

#### Discussion

The bottom bar conditonally applies a special visual treatment when it overlaps the main content of the subscription store view. The content within the bottom bar doesn’t scroll with the rest of the content in the main scroll view.

## See Also

- [static var automatic: CompactPickerSubscriptionStoreControlStyle.Placement](compactpickersubscriptionstorecontrolstyle/placement/automatic.md)
- [static var buttonsInBottomBar: CompactPickerSubscriptionStoreControlStyle.Placement](compactpickersubscriptionstorecontrolstyle/placement/buttonsinbottombar.md)
  A hybrid placement that positions subscription controls within the main scroll view, and places auxiliary buttons in the bottom bar.
- [static var scrollView: CompactPickerSubscriptionStoreControlStyle.Placement](compactpickersubscriptionstorecontrolstyle/placement/scrollview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/compactpickersubscriptionstorecontrolstyle/placement/bottombar)*