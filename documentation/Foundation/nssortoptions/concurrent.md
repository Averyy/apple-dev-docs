# concurrent

**Framework**: Foundation  
**Kind**: property

Specifies that the Block sort operation should be concurrent.

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
static var concurrent: NSSortOptions { get }
```

#### Discussion

This option is a hint and may be ignored by the implementation under some circumstances; the code of the Block must be safe against concurrent invocation.

## See Also

- [static var stable: NSSortOptions](nssortoptions/stable.md)
  Specifies that the sorted results should return compared items having equal value in the order they occurred originally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortoptions/concurrent)*