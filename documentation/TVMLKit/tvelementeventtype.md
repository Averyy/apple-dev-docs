# TVElementEventType

**Framework**: TVMLKit  
**Kind**: enum  
**Role**: Enumeration

The type of event that has been dispatched.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
enum TVElementEventType
```

```c
enum TVElementEventType : NSInteger;
```

## Topics

### Enumeration Cases
- [TVElementEventType.change](./tvelementeventtype/change.md)
  A change event has been dispatched.
- [TVElementEventType.highlight](./tvelementeventtype/highlight.md)
  A highlight event has been dispatched.
- [TVElementEventType.holdSelect](./tvelementeventtype/holdselect.md)
  A hold event has been dispatched.
- [TVElementEventType.play](./tvelementeventtype/play.md)
  A play event has been dispatched.
- [TVElementEventType.select](./tvelementeventtype/select.md)
  A select event has been dispatched.
### Initializers
- [init?(rawValue: Int)](./tvelementeventtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Dispatching Events
- [func dispatchEvent(type: TVElementEventType, canBubble: Bool, cancellable: Bool, extraInfo: [String : Any]?, completion: ((Bool, Bool) -> Void)?)](./tvviewelement/dispatchevent%28type,canbubble,cancellable,extrainfo,completion%29.md)
  Dispatches an event of a specific type to the JavaScript file.
- [func dispatchEvent(name: String, canBubble: Bool, cancellable: Bool, extraInfo: [String : Any]?, completion: ((Bool, Bool) -> Void)?)](./tvviewelement/dispatchevent%28name,canbubble,cancellable,extrainfo,completion%29.md)
  Dispatches a custom-named event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvelementeventtype)*