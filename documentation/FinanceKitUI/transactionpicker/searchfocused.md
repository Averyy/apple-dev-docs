# searchFocused(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func searchFocused(_ binding: FocusState<Bool>.Binding) -> some View
```

#### Return Value

The modified view.

#### Discussion

To control focus by matching a non-boolean value, use the `View/searchFocused(_:equals:)` modifier instead.

For more information about using searchable modifiers, refer to doc:Adding-a-search-interface-to-your-app.

## Parameters

- `condition`: The focus state to bind. When focus moves   to the associated search field, the binding sets the bound value to   . If a caller sets the value to    programmatically, then   focus moves to the search field. When focus leaves the search field,   the binding sets the value to  . If a caller sets the value to   , SwiftUI automatically dismisses focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/searchfocused(_:))*