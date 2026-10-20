# UIMenuElement.RepeatBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Possible repeat behaviors for a menu element.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum RepeatBehavior
```

```c
enum UIMenuElementRepeatBehavior : NSInteger;
```

## Topics

### Enumeration Cases
- [UIMenuElement.RepeatBehavior.automatic](./repeatbehavior/automatic.md)
  Automatically uses the appropriate repeat behavior for this element.
- [UIMenuElement.RepeatBehavior.nonRepeatable](./repeatbehavior/nonrepeatable.md)
  The element should not be repeatable.
- [UIMenuElement.RepeatBehavior.repeatable](./repeatbehavior/repeatable.md)
  The element should be allowed to repeat.
### Initializers
- [init?(rawValue: Int)](./repeatbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [UIMenuElement.Attributes](./attributes.md)
  Attributes that determine the style of the menu element.
- [UIMenuElement.State](./state.md)
  Constants that indicate the state of an action- or command-based menu element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement/repeatbehavior)*