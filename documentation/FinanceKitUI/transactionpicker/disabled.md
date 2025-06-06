# disabled(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Adds a condition that controls whether users can interact with this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func disabled(_ disabled: Bool) -> some View
```

#### Return Value

A view that controls whether users can interact with this view.

#### Discussion

The higher views in a view hierarchy can override the value you set on this view. In the following example, the button isn’t interactive because the outer `disabled(_:)` modifier overrides the inner one:

```None
HStack {
    Button(Text("Press")) {}
    .disabled(false)
}
.disabled(true)
```

## Parameters

- `disabled`: A Boolean value that determines whether users can   interact with this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/disabled(_:))*