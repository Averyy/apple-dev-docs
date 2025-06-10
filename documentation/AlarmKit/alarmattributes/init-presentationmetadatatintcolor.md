# init(presentation:metadata:tintColor:)

**Framework**: AlarmKit  
**Kind**: init

Creates an instance of an alarm UI.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
init(presentation: AlarmPresentation, metadata: Metadata? = nil, tintColor: Color)
```

## Parameters

- `presentation`: The content required for the various states of an alarm.
- `metadata`: The additional data that you can include in your attributes.
- `tintColor`: The tint color applied to the templated UI.

## See Also

- [var tintColor: Color](alarmattributes/tintcolor.md)
  The tint color applied to the templated UI.
- [var presentation: AlarmPresentation](alarmattributes/presentation.md)
  The content required for the various states of the UI.
- [var metadata: Metadata?](alarmattributes/metadata.md)
  The additional data you can include in your attributes.
- [AlarmAttributes.ContentState](alarmattributes/contentstate.md)
  The type alias for the structure that describes the content of an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmattributes/init(presentation:metadata:tintcolor:))*