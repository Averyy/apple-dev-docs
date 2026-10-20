# metadata

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

The additional data you can include in your attributes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var metadata: Metadata?
```

#### Discussion

The additional data can be information that describes extra UI features you want to include in your countdown UI.

## See Also

### Creating an alarm attribute
- [init(presentation: AlarmPresentation, metadata: Metadata?, tintColor: Color)](./init%28presentation,metadata,tintcolor%29.md)
  Creates an instance of an alarm UI.
- [var tintColor: Color](./tintcolor.md)
  The tint color applied to the templated UI.
- [var presentation: AlarmPresentation](./presentation.md)
  The content required for the various states of the UI.
- [AlarmAttributes.ContentState](./contentstate.md)
  The type alias for the structure that describes the content of an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmattributes/metadata)*