# accessibilityFocused(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Modifies this view by binding its accessibility element’s focus state to the given boolean state value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityFocused(_ condition: AccessibilityFocusState<Bool>.Binding) -> some View
```

#### Return Value

The modified view.

## Parameters

- `condition`: The accessibility focus state to bind. When   accessibility focus moves to the accessibility element of the   modified view, the focus value is set to  .   If the value is set to   programmatically, then accessibility   focus will move to accessibility element of the modified view.   The value will be set to   if accessibility focus leaves   the accessibility element of the modified view,   and accessibility focus will be dismissed automatically if the   value is set to   programmatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/accessibilityfocused(_:))*