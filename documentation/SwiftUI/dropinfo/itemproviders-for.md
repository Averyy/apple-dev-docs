# itemProviders(for:)

**Framework**: SwiftUI  
**Kind**: method

Finds item providers that conform to at least one of the specified uniform type identifiers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func itemProviders(for contentTypes: [UTType]) -> [NSItemProvider]
```

#### Return Value

The item providers that conforms to `contentTypes`.

#### Discussion

This function is only valid during the `performDrop()` action.

## Parameters

- `contentTypes`: The uniform type identifiers to query for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropinfo/itemproviders(for:))*