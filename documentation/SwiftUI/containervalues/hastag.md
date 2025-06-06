# hasTag(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns true if the container values contain a tag matching a given value.

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
func hasTag<V>(_ tag: V) -> Bool where V : Hashable
```

#### Return Value

If the container values has a tag matching the given value.

#### Discussion

Tag values are set using the `View/tag` modifier.

## Parameters

- `tag`: The tag value to check for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/containervalues/hastag(_:))*