# init(presentation:metadata:tintColor:)

**Framework**: AlarmKit  
**Kind**: init  
**Role**: Initializer

Creates an instance of an alarm UI.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(presentation: AlarmPresentation, metadata: Metadata? = nil, tintColor: Color)
```

## Parameters

- `presentation`: The content required for the various states of an alarm.
- `metadata`: The additional data that you can include in your attributes.
- `tintColor`: The tint color applied to the templated UI.

## See Also

### Creating an alarm attribute
- [var tintColor: Color](./tintcolor.md)
  The tint color applied to the templated UI.
- [var presentation: AlarmPresentation](./presentation.md)
  The content required for the various states of the UI.
- [var metadata: Metadata?](./metadata.md)
  The additional data you can include in your attributes.
- [AlarmAttributes.ContentState](./contentstate.md)
  The type alias for the structure that describes the content of an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmattributes/init(presentation:metadata:tintcolor:))*