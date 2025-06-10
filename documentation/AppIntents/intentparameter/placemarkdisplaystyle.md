# IntentParameter.PlacemarkDisplayStyle

**Framework**: App Intents  
**Kind**: enum

Describes a location’s display style in Shortcuts and Siri Suggestions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
enum PlacemarkDisplayStyle
```

## Topics

### Getting the display styles
- [IntentParameter.PlacemarkDisplayStyle.name](intentparameter/placemarkdisplaystyle/name.md)
  A display style that shows only the location’s city.
- [IntentParameter.PlacemarkDisplayStyle.address](intentparameter/placemarkdisplaystyle/address.md)
  A display style that shows the location’s full address.
- [IntentParameter.PlacemarkDisplayStyle.city](intentparameter/placemarkdisplaystyle/city.md)
  A display style that shows only the location’s city.
### Operators
- [static func == (IntentParameter<Value>.PlacemarkDisplayStyle, IntentParameter<Value>.PlacemarkDisplayStyle) -> Bool](intentparameter/placemarkdisplaystyle/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](intentparameter/placemarkdisplaystyle/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intentparameter/placemarkdisplaystyle/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](intentparameter/placemarkdisplaystyle/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var displayStyle: IntentParameter<Value>.PlacemarkDisplayStyle?](intentparameter/displaystyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/placemarkdisplaystyle)*