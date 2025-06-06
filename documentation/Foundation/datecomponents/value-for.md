# value(for:)

**Framework**: Foundation  
**Kind**: method

Returns the value of one of the properties, using an enumeration value instead of a property name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func value(for component: Calendar.Component) -> Int?
```

#### Discussion

The calendar and timeZone and isLeapMonth property values cannot be retrieved by this method.

## See Also

- [func setValue(Int?, for: Calendar.Component)](datecomponents/setvalue(_:for:).md)
  Set the value of one of the properties, using an enumeration value instead of a property name.
- [Calendar.Component](calendar/component.md)
  An enumeration for the various components of a calendar date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/value(for:))*