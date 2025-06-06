# delegate

**Framework**: AVKit  
**Kind**: property

The delegate object for the route picker.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 11.0+

## Declaration

```swift
@MainActor
weak var delegate: (any AVRoutePickerViewDelegate)? { get set }
```

## See Also

- [protocol AVRoutePickerViewDelegate](avroutepickerviewdelegate.md)
  A protocol that defines the methods to adopt to respond to route picker view presentation events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avroutepickerview/delegate)*