# accessibilityFocused(_:equals:)

**Framework**: SwiftUI  
**Kind**: method

Modifies this view by binding its accessibility element’s focus state to the given state value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
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

## See Also

- [func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some View](view/accessibilityfocused(_:).md)
  Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [struct AccessibilityFocusState](accessibilityfocusstate.md)
  A property wrapper type that can read and write a value that SwiftUI updates as the focus of any active accessibility technology, such as VoiceOver, changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityfocused(_:equals:))*