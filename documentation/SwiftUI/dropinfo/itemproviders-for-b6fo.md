# itemProviders(for:)

**Framework**: SwiftUI  
**Kind**: method

Returns an array of items that each conform to at least one of the specified uniform type identifiers.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func itemProviders(for types: [String]) -> [NSItemProvider]
```

#### Discussion

This function is only valid during the `performDrop()` action.

## See Also

- [func hasItemsConforming(to: [String]) -> Bool](dropinfo/hasitemsconforming(to:)-4qeez.md)
  Returns whether at least one item conforms to at least one of the specified uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropinfo/itemproviders(for:)-b6fo)*