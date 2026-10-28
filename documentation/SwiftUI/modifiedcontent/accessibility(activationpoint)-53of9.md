# accessibility(activationPoint:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies the unit point where activations occur in the view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: accessibilityActivationPoint(_:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: accessibilityActivationPoint(_:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: accessibilityActivationPoint(_:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: accessibilityActivationPoint(_:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: accessibilityActivationPoint(_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: accessibilityActivationPoint(_:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: accessibilityActivationPoint(_:))

> **Deprecated**: Use [`accessibilityActivationPoint(_:)`](./accessibilityactivationpoint%28_%29-74w70.md) instead.

## Declaration

```swift
nonisolated
func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Content, Modifier>
```

Available when `Modifier` is `AccessibilityAttachmentModifier`.

**Other overloads**:

```swift
nonisolated
func accessibility(activationPoint: CGPoint) -> ModifiedContent<Content, Modifier>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibility(activationpoint:)-53of9)*