# accessibilityValue(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
@export(implementation)
nonisolated func accessibilityValue(_ valueResource: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Content, Modifier>
```

Available when `Modifier` is `AccessibilityAttachmentModifier`.

**Other overloads**:

```swift
nonisolated
func accessibilityValue(_ valueDescription: Text, isEnabled: Bool) -> ModifiedContent<Content, Modifier>
```

```swift
nonisolated
func accessibilityValue(_ valueKey: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Content, Modifier>
```

```swift
nonisolated
func accessibilityValue<S>(_ value: S, isEnabled: Bool) -> ModifiedContent<Content, Modifier> where S : StringProtocol
```

## Discussion

Use this method to describe the value represented by a view, but only if that’s different than the view’s label. For example, for a slider that you label as “Volume” using accessibilityLabel(), you can provide the current volume setting, like “60%”, using accessibilityValue().

## Parameters

- `valueResource`: The accessibility value to apply.
- `isEnabled`: If true the accessibility value is applied; otherwise the accessibility value is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityvalue(_:isenabled:))*