# setSet(_:)

**Framework**: Foundation  
**Kind**: method

Empties the receiving set, then adds each object contained in another given set.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setSet(_ otherSet: Set<AnyHashable>)
```

## Parameters

- `otherSet`: The set whose members replace the receiving set’s content.

## See Also

- [func union(Set<AnyHashable>)](nsmutableset/union(_:).md)
  Adds each object in another given set to the receiving set, if not present.
- [func minus(Set<AnyHashable>)](nsmutableset/minus(_:).md)
  Removes each object in another given set from the receiving set, if present.
- [func intersect(Set<AnyHashable>)](nsmutableset/intersect(_:).md)
  Removes from the receiving set each object that isn’t a member of another given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/setset(_:))*