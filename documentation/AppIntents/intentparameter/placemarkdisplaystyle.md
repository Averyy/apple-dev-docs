# IntentParameter.PlacemarkDisplayStyle

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

Describes a location’s display style in Shortcuts and Siri Suggestions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
enum PlacemarkDisplayStyle
```

Available when `Value` conforms to `_IntentValue` and `Sendable`.

## Topics

### Getting the display styles
- [IntentParameter.PlacemarkDisplayStyle.name](./placemarkdisplaystyle/name.md)
  A display style that shows only the location’s city.
- [IntentParameter.PlacemarkDisplayStyle.address](./placemarkdisplaystyle/address.md)
  A display style that shows the location’s full address.
- [IntentParameter.PlacemarkDisplayStyle.city](./placemarkdisplaystyle/city.md)
  A display style that shows only the location’s city.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing the display style
- [var displayStyle: IntentParameter<Value>.PlacemarkDisplayStyle?](./displaystyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/placemarkdisplaystyle)*