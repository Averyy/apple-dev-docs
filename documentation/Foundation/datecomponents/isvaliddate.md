# isValidDate

**Framework**: Foundation  
**Kind**: property

Indicates whether the current combination of properties represents a date which exists in the current calendar.

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
var isValidDate: Bool { get }
```

#### Discussion

This method is not appropriate for use on `DateComponents` values which are specifying relative quantities of calendar components.

Except for some trivial cases (e.g., ‘seconds’ should be 0 - 59 in any calendar), this method is not necessarily cheap.

If the time zone property is set in the `DateComponents`, it is used.

The calendar property must be set, or the result is always `false`.

## See Also

- [func isValidDate(in: Calendar) -> Bool](datecomponents/isvaliddate(in:).md)
  Indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [var date: Date?](datecomponents/date.md)
  The date calculated from the current components using the stored calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/isvaliddate)*