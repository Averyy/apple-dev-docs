# subtype

**Framework**: UIKit  
**Kind**: property

Returns the subtype of the event.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var subtype: UIEvent.EventSubtype { get }
```

#### Discussion

The [`UIEvent.EventSubtype`](uievent/eventsubtype.md) constant returned by this property indicates the subtype of the event in relation to the general type, which you can retrieve from the [`type`](uievent/type.md) property.

## See Also

- [var type: UIEvent.EventType](uievent/type.md)
  Returns the type of the event.
- [UIEvent.EventType](uievent/eventtype.md)
  Constants that specify the general type of an event.
- [UIEvent.EventSubtype](uievent/eventsubtype.md)
  Constants that specify the subtype of the event in relation to its general type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/subtype)*