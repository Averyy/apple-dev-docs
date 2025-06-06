# read(from:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Reads the trait value from the trait collection, and returns the equivalent environment value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static func read(from traitCollection: UITraitCollection) -> Self.Value
```

## Parameters

- `traitCollection`: The trait collection to read from.

## See Also

- [static func write(to: inout any UIMutableTraits, value: Self.Value)](uitraitbridgedenvironmentkey/write(to:value:).md)
  Writes the equivalent trait value for the environment value into the mutable traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uitraitbridgedenvironmentkey/read(from:))*