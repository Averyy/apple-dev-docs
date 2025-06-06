# isSelected

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates whether the picker option is in a selected state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
let isSelected: Bool
```

#### Discussion

Use the [`isSelected`](subscriptionstorecontrolstyleconfiguration/pickeroption/isselected.md) property to display a selection indicator, such as a checkmark, in its correct state. The following code example shows a checkmark when [`isSelected`](subscriptionstorecontrolstyleconfiguration/pickeroption/isselected.md) is true:

```swift
SubscriptionPickerOption(option) { pickerOption in 
HStack {
    Text(pickerOption.displayName)
    Spacer()
    Image(systemName: "checkmark")
        .opacity(pickerOption.isSelected ? 1 : 0)
    }
}
```

The [`SubscriptionStorePicker`](subscriptionstorepicker.md) automatically updates the picker’s selection state as customers interact with your picker. However, the [`SubscriptionStorePicker`](subscriptionstorepicker.md) doesn’t display selection indicators. Your app needs to display selection indicators in the picker option label.

Use the [`SubscriptionStoreControlStyleConfiguration.PickerOption`](subscriptionstorecontrolstyleconfiguration/pickeroption.md) value, which represents the properties of a subscription picker option’s label, to display the selection indicator.

## See Also

- [var subscription: Product](subscriptionstorecontrolstyleconfiguration/pickeroption/subscription.md)
  The auto-renewable subscription that the picker option represents.
- [var activeOffer: Product.SubscriptionOffer?](subscriptionstorecontrolstyleconfiguration/pickeroption/activeoffer.md)
- [var icon: SubscriptionStoreControlStyleConfiguration.Icon?](subscriptionstorecontrolstyleconfiguration/pickeroption/icon.md)
  The subscription option’s icon.
- [var id: Product.ID](subscriptionstorecontrolstyleconfiguration/pickeroption/id.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/isselected)*