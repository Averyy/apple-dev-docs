# SubscriptionStoreControlBackground

**Framework**: StoreKit  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
struct SubscriptionStoreControlBackground
```

## Topics

### Background types
- [static var automatic: SubscriptionStoreControlBackground](subscriptionstorecontrolbackground/automatic.md)
- [static var gradientMaterial: SubscriptionStoreControlBackground](subscriptionstorecontrolbackground/gradientmaterial.md)
- [static var gradientMaterialOnScroll: SubscriptionStoreControlBackground](subscriptionstorecontrolbackground/gradientmaterialonscroll.md)

## See Also

- [nonisolated func containerBackground<S>(_ style: S, for container: ContainerBackgroundPlacement) -> some View where S : ShapeStyle
](../SwiftUI/View/containerBackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [nonisolated func containerBackground<V>(for container: ContainerBackgroundPlacement, alignment: Alignment = .center, @ViewBuilder content: () -> V) -> some View where V : View
](../SwiftUI/View/containerBackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [nonisolated func subscriptionStoreControlBackground(_ backgroundStyle: some ShapeStyle) -> some View
](../SwiftUI/View/subscriptionStoreControlBackground(_:)-7jxa9.md)
  Set a shape style to use for the background of subscription store view controls within the view.
- [nonisolated func subscriptionStoreControlBackground(_ backgroundStyle: SubscriptionStoreControlBackground) -> some View
](../SwiftUI/View/subscriptionStoreControlBackground(_:)-7ev89.md)
  Set a standard effect to use for the background of subscription store view controls within the view.
- [static var subscriptionStore: ContainerBackgroundPlacement { get }](../SwiftUI/ContainerBackgroundPlacement/subscriptionStore.md)
  An automatic placement within a subscription store view, based on the view’s context.
- [static var subscriptionStoreHeader: ContainerBackgroundPlacement { get }](../SwiftUI/ContainerBackgroundPlacement/subscriptionStoreHeader.md)
  A background placement behind the marketing content of a subscription store view.
- [static var subscriptionStoreFullHeight: ContainerBackgroundPlacement { get }](../SwiftUI/ContainerBackgroundPlacement/subscriptionStoreFullHeight.md)
  A background placement that spans the full height of a subscription store view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolbackground)*