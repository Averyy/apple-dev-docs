# TVElementEventType

**Framework**: TVMLKit  
**Kind**: enum

The type of event that has been dispatched.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
enum TVElementEventType
```

## Topics

### Enumeration Cases
- [TVElementEventType.change](tvelementeventtype/change.md)
  A change event has been dispatched.
- [TVElementEventType.highlight](tvelementeventtype/highlight.md)
  A highlight event has been dispatched.
- [TVElementEventType.holdSelect](tvelementeventtype/holdselect.md)
  A hold event has been dispatched.
- [TVElementEventType.play](tvelementeventtype/play.md)
  A play event has been dispatched.
- [TVElementEventType.select](tvelementeventtype/select.md)
  A select event has been dispatched.
### Initializers
- [init?(rawValue: Int)](tvelementeventtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func dispatchEvent(type: TVElementEventType, canBubble: Bool, cancellable: Bool, extraInfo: [String : Any]?, completion: ((Bool, Bool) -> Void)?)](tvviewelement/dispatchevent(type:canbubble:cancellable:extrainfo:completion:).md)
  Dispatches an event of a specific type to the JavaScript file.
- [func dispatchEvent(name: String, canBubble: Bool, cancellable: Bool, extraInfo: [String : Any]?, completion: ((Bool, Bool) -> Void)?)](tvviewelement/dispatchevent(name:canbubble:cancellable:extrainfo:completion:).md)
  Dispatches a custom-named event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvelementeventtype)*