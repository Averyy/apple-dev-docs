# TVElementResettableProperty

**Framework**: TVMLKit  
**Kind**: enum  
**Role**: Enumeration

The types of properties that can be reset to their default values.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
enum TVElementResettableProperty
```

```c
enum TVElementResettableProperty : NSInteger;
```

## Topics

### Constants
- [TVElementResettableProperty.updateType](./tvelementresettableproperty/updatetype.md)
  The [`updateType`](./tvviewelement/updatetype.md) property is reset to [`TVElementUpdateType.none`](./tvelementupdatetype/none.md).
- [TVElementResettableProperty.autoHighlightIdentifier](./tvelementresettableproperty/autohighlightidentifier.md)
  The [`autoHighlightIdentifier`](./tvviewelement/autohighlightidentifier.md) property is reset to `nil`.
### Initializers
- [init?(rawValue: Int)](./tvelementresettableproperty/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Resetting a Property’s Value
- [func resetProperty(TVElementResettableProperty)](./tvviewelement/resetproperty%28_%29.md)
  Resets the property to its default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvelementresettableproperty)*