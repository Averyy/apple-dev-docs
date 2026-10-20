# type

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the type of the event.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var type: UIEvent.EventType { get }
```

```objc
@property (nonatomic, readonly) UIEventType type;
```

#### Discussion

The [`UIEvent.EventType`](./eventtype.md) constant returned by this property indicates the general type of this event — for example, whether it’s a touch or motion event.

## See Also

### Getting the event type
- [UIEvent.EventType](./eventtype.md)
  Constants that specify the general type of an event.
- [var subtype: UIEvent.EventSubtype](./subtype.md)
  Returns the subtype of the event.
- [UIEvent.EventSubtype](./eventsubtype.md)
  Constants that specify the subtype of the event in relation to its general type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/type)*