# isValidDate

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isValidDate: Bool { get }
```

#### Discussion

If the [`timeZone`](nsdatecomponents/timezone.md) property is set on the receiver, the time zone property value is used. If the [`calendar`](nsdatecomponents/calendar.md) property is not set on the receiver, `nil` is returned.

## See Also

- [func isValidDate(in: Calendar) -> Bool](nsdatecomponents/isvaliddate(in:).md)
  Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [var date: Date?](nsdatecomponents/date.md)
  The date calculated from the current components using the stored calendar.
- [Undefined Components](1430344-undefined-components.md)
  Constants that denote that the value of a date component is undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/isvaliddate)*