# stable

**Framework**: Foundation  
**Kind**: property

Specifies that the sorted results should return compared items having equal value in the order they occurred originally.

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
static var stable: NSSortOptions { get }
```

#### Discussion

If this option is unspecified, equal objects may, or may not be returned in their original order.

## See Also

- [static var concurrent: NSSortOptions](nssortoptions/concurrent.md)
  Specifies that the Block sort operation should be concurrent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortoptions/stable)*