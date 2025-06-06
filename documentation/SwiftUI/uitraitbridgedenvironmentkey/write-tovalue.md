# write(to:value:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Writes the equivalent trait value for the environment value into the mutable traits.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static func write(to mutableTraits: inout any UIMutableTraits, value: Self.Value)
```

## Parameters

- `mutableTraits`: The mutable traits to write to.
- `value`: The environment value to write.

## See Also

- [static func read(from: UITraitCollection) -> Self.Value](uitraitbridgedenvironmentkey/read(from:).md)
  Reads the trait value from the trait collection, and returns the equivalent environment value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uitraitbridgedenvironmentkey/write(to:value:))*