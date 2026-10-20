# string(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a string representation of a specified date that the system formats using the receiver’s current settings.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func string(from date: Date) -> String
```

```objc
- (NSString *) stringFromDate:(NSDate *) date;
```

#### Return Value

A string representation of `date`.

#### Discussion

For more information about using [`DateFormatter`](../dateformatter.md) to produce a string representation of a date, see [Working With User-Visible Representations of Dates and Times](../dateformatter.md#Working-With-User-Visible-Representations-of-Dates-and-Times). For a sample code playground, see [Displaying Human-Friendly Content](../displaying-human-friendly-content.md).

## Parameters

- `date`: The date to format.

## See Also

### Converting Objects
- [func date(from: String) -> Date?](./date%28from%29.md)
  Returns a date representation of a specified string that the system interprets using the receiver’s current settings.
- [class func localizedString(from: Date, dateStyle: DateFormatter.Style, timeStyle: DateFormatter.Style) -> String](./localizedstring%28from,datestyle,timestyle%29.md)
  Returns a string representation of a specified date, that the system formats for the current locale using the specified date and time styles.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, range: UnsafeMutablePointer<NSRange>?) throws](./getobjectvalue%28_,for,range%29.md)
  Returns by reference a date representation of a specified string and its date range, as well as a Boolean value that indicates whether the system can parse the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/string(from:))*