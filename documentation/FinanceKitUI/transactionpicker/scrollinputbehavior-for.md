# scrollInputBehavior(_:for:)

**Framework**: FinanceKitUI  
**Kind**: method

Enables or disables scrolling in scrollable views when using particular inputs.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency func scrollInputBehavior(_ behavior: ScrollInputBehavior, for input: ScrollInputKind) -> some View
```

#### Discussion

In contrast to `View/scrollDisabled(_:)`, this modifier will enable or disable scrolling only for particular inputs. The following, for instance, disables double-tap-to-scroll on watchOS while preserving the ability to scroll via touch and the Digital Crown:

```None
ScrollView(...)
    .scrollInputBehavior(.disabled, for: .handGestureShortcut)
```

If `scrollDisabled(true)` has been applied to this view, scrolling will be disabled for all inputs and this modifier cannot be used to re-enable scrolling.

## Parameters

- `behavior`: Whether scrolling should be enabled or disabled for this   input.
- `input`: The input for which to enable or disable scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/scrollinputbehavior(_:for:))*