# itemProviders(for:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns an array of items that each conform to at least one of the specified uniform type identifiers.

**Availability**:
- iOS 13.4+ - Deprecated in 27.2
- iPadOS 13.4+ - Deprecated in 27.2
- Mac Catalyst 13.4+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`itemProviders(for:)`](./itemproviders%28for%29-93409.md) instead.

## Declaration

```swift
func itemProviders(for types: [String]) -> [NSItemProvider]
```

**Other overloads**:

```swift
func itemProviders(for contentTypes: [UTType]) -> [NSItemProvider]
```

## Discussion

This function is only valid during the `performDrop()` action.

## See Also

### Deprecated symbols
- [func hasItemsConforming(to: [String]) -> Bool](./hasitemsconforming%28to%29-4qeez.md)
  Returns whether at least one item conforms to at least one of the specified uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropinfo/itemproviders(for:)-b6fo)*