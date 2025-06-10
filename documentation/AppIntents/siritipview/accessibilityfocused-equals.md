# accessibilityFocused(_:equals:)

**Framework**: App Intents  
**Kind**: method

Modifies this view by binding its accessibility element’s focus state to the given state value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityFocused<Value>(_ binding: AccessibilityFocusState<Value>.Binding, equals value: Value) -> some View where Value : Hashable
```

#### Return Value

The modified view.

## Parameters

- `binding`: The state binding to register. When accessibility focus moves to the   accessibility element of the modified view, SwiftUI sets the bound value to the corresponding   match value. If you set the state value programmatically to the matching value, then   accessibility focus moves to the accessibility element of the modified view. SwiftUI sets   the value to   if accessibility focus leaves the accessibility element associated with the   modified view, and programmatically setting the value to   dismisses focus automatically.
- `value`: The value to match against when determining whether the   binding should change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/accessibilityfocused(_:equals:))*