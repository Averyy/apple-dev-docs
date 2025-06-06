# hash(into:)

**Framework**: RealityKit  
**Kind**: method

Hashes the essential components of the target by feeding them into the given hash function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hash function to use when combining the components of   the target.

## See Also

- [static func == (AnchoringComponent.Target, AnchoringComponent.Target) -> Bool](anchoringcomponent/target-swift.enum/==(_:_:).md)
  Indicates whether two targets are equal.
- [static func != (Self, Self) -> Bool](anchoringcomponent/target-swift.enum/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [var hashValue: Int](anchoringcomponent/target-swift.enum/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/hash(into:))*