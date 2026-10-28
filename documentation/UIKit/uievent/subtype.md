# subtype

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the subtype of the event.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var subtype: UIEvent.EventSubtype { get }
```

```objc
@property (nonatomic, readonly) UIEventSubtype subtype;
```

## Discussion

The [`UIEvent.EventSubtype`](./eventsubtype.md) constant returned by this property indicates the subtype of the event in relation to the general type, which you can retrieve from the [`type`](./type.md) property.

## See Also

### Getting the event type
- [var type: UIEvent.EventType](./type.md)
  Returns the type of the event.
- [UIEvent.EventType](./eventtype.md)
  Constants that specify the general type of an event.
- [UIEvent.EventSubtype](./eventsubtype.md)
  Constants that specify the subtype of the event in relation to its general type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/subtype)*