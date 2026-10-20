# UIAccessibilityCustomRotor.Direction

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the search direction.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum Direction
```

```c
enum UIAccessibilityCustomRotorDirection : NSInteger;
```

## Topics

### Constants
- [UIAccessibilityCustomRotor.Direction.previous](./direction/previous.md)
  The previous search item.
- [UIAccessibilityCustomRotor.Direction.next](./direction/next.md)
  The next search item.
### Initializers
- [init?(rawValue: Int)](./direction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Navigating to the next item
- [var itemSearchBlock: UIAccessibilityCustomRotor.Search](./itemsearchblock.md)
  The block for retrieving the next or previous rotor.
- [UIAccessibilityCustomRotor.Search](./search.md)
  The block type for retrieving the next or previous rotor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/direction)*