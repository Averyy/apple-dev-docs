# setValue(_:for:)

**Framework**: Foundation  
**Kind**: method

Set the value of one of the properties, using an enumeration value instead of a property name.

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
mutating func setValue(_ value: Int?, for component: Calendar.Component)
```

#### Discussion

The calendar and timeZone and isLeapMonth properties cannot be set by this method.

## See Also

- [func value(for: Calendar.Component) -> Int?](datecomponents/value(for:).md)
  Returns the value of one of the properties, using an enumeration value instead of a property name.
- [Calendar.Component](calendar/component.md)
  An enumeration for the various components of a calendar date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/setvalue(_:for:))*