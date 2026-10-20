# displayStyle

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

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
final var displayStyle: IntentParameter<Value>.PlacemarkDisplayStyle? { get }
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `CLPlacemark`.

## See Also

### Accessing the display style
- [IntentParameter.PlacemarkDisplayStyle](./placemarkdisplaystyle.md)
  Describes a location’s display style in Shortcuts and Siri Suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/displaystyle)*