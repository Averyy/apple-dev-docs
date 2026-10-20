# AlarmAttributes.ContentState

**Framework**: AlarmKit  
**Kind**: typealias  
**Role**: Type Alias

The type alias for the structure that describes the content of an alarm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
typealias ContentState = AlarmPresentationState
```

## See Also

### Creating an alarm attribute
- [init(presentation: AlarmPresentation, metadata: Metadata?, tintColor: Color)](./init%28presentation,metadata,tintcolor%29.md)
  Creates an instance of an alarm UI.
- [var tintColor: Color](./tintcolor.md)
  The tint color applied to the templated UI.
- [var presentation: AlarmPresentation](./presentation.md)
  The content required for the various states of the UI.
- [var metadata: Metadata?](./metadata.md)
  The additional data you can include in your attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmattributes/contentstate)*