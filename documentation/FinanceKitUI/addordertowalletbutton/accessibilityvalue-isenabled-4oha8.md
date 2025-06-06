# accessibilityValue(_:isEnabled:)

**Framework**: FinanceKitUI  
**Kind**: method

Adds a textual description of the value that the view contains.

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
nonisolated
func accessibilityValue(_ valueDescription: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this method to describe the value represented by a view, but only if that’s different than the view’s label. For example, for a slider that you label as “Volume” using accessibilityLabel(), you can provide the current volume setting, like “60%”, using accessibilityValue().

## Parameters

- `valueDescription`: The accessibility value to apply.
- `isEnabled`: If true the accessibility value is applied; otherwise   the accessibility value is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/accessibilityvalue(_:isenabled:)-4oha8)*