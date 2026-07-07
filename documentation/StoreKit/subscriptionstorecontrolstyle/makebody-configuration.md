# makeBody(configuration:)

**Framework**: StoreKit  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a subscription store control.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Return Value

A view which provides UI controls to subscribe to a subscription service.

#### Discussion

Implement this method to define a custom subscription store control style which conforms to the [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md). Use the `configuration` input — a value of [`SubscriptionStoreControlStyleConfiguration`](subscriptionstorecontrolstyleconfiguration.md) — to access the collection of subscription options to merchandise, and other properties of the controls. Return a view that provides controls for someone to choose an option from the configuration and subscribe. The following code example defines a style that adds price comparison captions to buttons:

```swift
struct PriceComparisonButtonsSubscriptionStoreControlStyle: SubscriptionStoreControlStyle {

    func makeBody(configuration: Configuration) -> some View {
        ForEach(configuration.options) { option in
            VStack {
                Button(localizedPrice(for: option), action: option.subscribe)
                if let priceComparison = priceComparison(for: option, allOptions: configuration.allOptions) {
                    Text(priceComparison)
                }
            }
        }
    }

    // Helper methods for localizing text
    
    private func localizedPrice(for option: Configuration.Option) -> LocalizedStringKey {
        // Use 'displayPrice' and 'subscriptionPeriod' on 'option' to localize the price.
        // For example: "$9.99/month"
    }
    
    private func priceComparison(for option: Configuration.Option, allOptions: [Product]) -> LocalizedStringKey? {
        guard let subscriptionPeriod = option.subscriptionPeriod, subscriptionPeriod != .monthly else {
            return nil
        }
        let monthlyOption = allOptions.first { otherOption in 
            otherOption.subscriptionPeriod == .monthly && otherOption.groupLevel == option.groupLevel
        }
        guard let monthlyOption else { 
            return nil
        }
        // Create a localized string to represent the savings of subscribing to 'option' compared to paying per
        // month with 'monthlyOption'. For example, "Save $20.00 per year compared to the monthly option".
    }
}
```

The `PriceComparisonButtonsSubscriptionStoreControlStyle` structure in the example code provides a button to subscribe to each option in the [`options`](subscriptionstorecontrolstyleconfiguration/options.md) property of the `configuration`, along with an optional informative caption for options with durations longer than one month. By calling the [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) method when a button is triggered, the subscription store view automatically manages a purchase task with the appropriate purchase options. The buttons automatically use the same button style as standard subscription store control styles, but you can customize this using [`buttonStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/buttonStyle(_:)-66fbx).

Since the control style creates a [`VStack`](https://developer.apple.com/documentation/SwiftUI/VStack) for each option, the subscription store view automatically lays out the stacks appropriately. You could instead provide an explicit layout container around [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach) to customize the spacing and alignment of the buttons.

To handle cases where the monthly plans aren’t visible, the control style uses the [`allOptions`](subscriptionstorecontrolstyleconfiguration/alloptions.md) property to compute price comparsions instead of [`options`](subscriptionstorecontrolstyleconfiguration/options.md).

The control style reads properties of [`Product.SubscriptionInfo`](product/subscriptioninfo.md) directly on the [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) using dynamic member lookup, such as [`subscriptionPeriod`](product/subscriptioninfo/subscriptionperiod.md).

Whenever any of the properties of `configuration` change, the system calls your [`makeBody(configuration:)`](subscriptionstorecontrolstyle/makebody(configuration:).md) method again to display an updated view.

The above example provides a button per plan, but not all control styles need to work this way. For example, you could combine multiple controls together with buttons, such as [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker) or [`Toggle`](https://developer.apple.com/documentation/SwiftUI/Toggle), and use state to implement more complicated interactions.

##### Modifying Subviews of Standard Control Styles

The `PriceComparisonButtonsSubscriptionStoreControlStyle` in the example code above uses the [`Button`](https://developer.apple.com/documentation/SwiftUI/Button) type to add buttons, but you can also use the [`SubscriptionStoreButton`](subscriptionstorebutton.md) view to modify the standard subscribe button. When within the scope of a type conforming to [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md), you can simply spell this view as `SubscribeButton`.

For example, the following update to the `PriceComparisonButtonsSubscriptionStoreControlStyle` example code uses `SubscribeButton` instead of [`Button`](https://developer.apple.com/documentation/SwiftUI/Button):

```swift
struct PriceComparisonButtonsSubscriptionStoreControlStyle: SubscriptionStoreControlStyle {

    func makeBody(configuration: Configuration) -> some View {
        ForEach(configuration.options) { option in
            VStack {
                SubscribeButton(option)
                if let priceComparison = priceComparison(for: option, allOptions: configuration.allOptions) {
                    Text(priceComparison)
                }
            }
            .subscriptionStoreButtonLabel(.price)
        }
    }

    // Helper method for localizing text     
    private func priceComparison(for option: Configuration.Option, allOptions: [Product]) -> LocalizedStringKey? {
        // Create a localized string to represent the savings of subscribing to 'option' compared to paying per
        // month with 'monthlyOption'. For example, "Save $20.00 per year compared to the monthly option".
    }
}
```

The updated custom style no longer needs to implement a custom `localizedPrice(for:)` method, instead the `SubscribeButton` automatically creates the localized label. The custom style uses the `subscriptionStoreButtonLabel(_:)` view modifier to only show the price in the button’s label.

You can also create custom control styles which modify the standard subscription picker control by using the [`SubscriptionStorePicker`](subscriptionstorepicker.md) type. When within the scope of a type conforming to [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md), you can simply spell this view as `SubscriptionPicker`. For example, you can create a style to modify the standard subscription picker to use a custom label for the picker options:

```swift
struct SimpleCustomPickerOptionLabelSubscriptionStoreControlStyle: SubscriptionStoreControlStyle {

    func makeBody(configuration: Configuration) -> some View {
        SubscriptionPicker(configuration) { option in 
            HStack {
                VStack {
                    Text(option.displayName)
                    if option.activeOffer != nil {
                        Label("Special Offer", systemImage: "star")
                            .symbolVariant(.fill)
                            .foregroundStyle(.tint)
                            .font(.caption)
                            .padding(4)
                            .background(.secondary, .rect(cornerRadius: 4)
                    }
                }
                Spacer()
                Image(systemName: "checkmark")
                    .foregroundStyle(.tint)
                    .opacity(option.isSelected ? 1.0 : 0.0)
            }
        } confirmation: { option in 
            SubscribeButton(option)
        }
    }
}
```

The `SimpleCustomPickerOptionLabelSubscriptionStoreControlStyle` in the example code provides a picker control to select a plan from the `configuration` by providing the `configuration` value to the `SubscriptionPicker` view.

The first closure provided to the subscription picker receives a [`SubscriptionStoreControlStyleConfiguration.PickerOption`](subscriptionstorecontrolstyleconfiguration/pickeroption.md) value, and returns a view to use as the label for each picker option. The subscription picker calls this closure once for each option in the configuration’s [`options`](https://developer.apple.com/documentation/IOUSBHost/IOUSBHostIsochronousTransaction/options) property. The style uses the [`displayName`](product/displayname.md) property of [`Product`](product.md) via dynamic member lookup to indicate which plan the picker option corresponds to. If the subscription store is configured to merchandise an offer, the custom style shows a label by checking `offer` . The style uses the [`isSelected`](subscriptionstorecontrolstyleconfiguration/pickeroption/isselected.md) property to adjust the visibility of a checkmark indicating the selected plan. The [`isSelected`](subscriptionstorecontrolstyleconfiguration/pickeroption/isselected.md) property is available instead of [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) when declaring subscription picker option labels.

The second closure provided to the subscription picker receives a [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) value, providing a control to confirm the currently selected plan. The custom style only provides custom picker option, and uses the standard subscribe button for the confirmation content. The standard subscribe button displays the price of the selected option.

You can also access the standard subscription picker option label by using [`SubscriptionStorePickerOption`](subscriptionstorepickeroption.md).

## Parameters

- `configuration`: The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.

## See Also

- [SubscriptionStoreControlStyle.Configuration](subscriptionstorecontrolstyle/configuration.md)
  The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.
- [SubscriptionStoreControlStyle.SubscribeButton](subscriptionstorecontrolstyle/subscribebutton.md)
  A button for subscribing to an in-app subscription.
- [SubscriptionStoreControlStyle.SubscriptionPicker](subscriptionstorecontrolstyle/subscriptionpicker.md)
  A composite control for selecting a subscription option and confirming the subscription.
- [SubscriptionStoreControlStyle.SubscriptionPickerOption](subscriptionstorecontrolstyle/subscriptionpickeroption.md)
  A subscription option within a subscription picker control.
- [struct SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey.md)
  A placement for a subscription store control in a store view.
- [associatedtype Placement : SubscriptionStoreControlPlacement = AutomaticSubscriptionStoreControlPlacement](subscriptionstorecontrolstyle/placement.md)
  The placement of subscription controls in a subscription store.
- [associatedtype Body : View](subscriptionstorecontrolstyle/body.md)
  A view that represents the body of a subscription store control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle/makebody(configuration:))*