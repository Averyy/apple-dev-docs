# referenceDate

**Framework**: Foundation  
**Kind**: property

Where units have variable length (number of days in a month, number of hours in a day, etc.), `NSDateComponentsFormatter` will calculate as though counting from the date specified by the `referenceDate` in the appropriate calendar. Defaults to `[NSDate dateWithTimeIntervalSinceReferenceDate:0]` at the time of the `-stringForObjectValue:` call if not set. Set to `nil` to get the default behavior.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var referenceDate: Date? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/referencedate)*