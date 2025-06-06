# monospaced(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func monospaced(_ isActive: Bool = true) -> some View
```

#### Return Value

A view whose child views’ fonts use fixed-width characters, while leaving other characters proportionally spaced.

#### Discussion

If a child view’s base font doesn’t support fixed-width, the font remains unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/monospaced(_:))*