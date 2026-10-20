# string(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a formatted string for a date relative to the current date and time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func string(for obj: Any?) -> String?
```

```objc
- (NSString *) stringForObjectValue:(id) obj;
```

#### Return Value

A string that represents the date interval between a date and the current date and time, or `nil` if obj isn’t an instance of [`NSDate`](../nsdate.md).

#### Discussion

To determine the relative interval, the formatter uses [`date`](../nsdate/date.md) as the reference date.

## Parameters

- `obj`: A date object to format.

## See Also

### Converting Dates to Formatted Strings
- [func localizedString(for: Date, relativeTo: Date) -> String](./localizedstring%28for,relativeto%29.md)
  Formats the date interval from the reference date to the specified date using the formatter’s calendar.
- [func localizedString(from: DateComponents) -> String](./localizedstring%28from%29.md)
  Formats a relative time represented by the specified date components.
- [func localizedString(fromTimeInterval: TimeInterval) -> String](./localizedstring%28fromtimeinterval%29.md)
  Formats the specified time interval using the formatter’s calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/relativedatetimeformatter/string(for:))*