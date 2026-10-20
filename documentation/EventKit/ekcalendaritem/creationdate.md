# creationDate

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The date that this calendar item was created.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var creationDate: Date? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSDate * creationDate;
```

#### Discussion

If `nil`, this property was not set or was synced in this state.

## See Also

### Accessing Calendar Item Properties
- [var calendar: EKCalendar!](./calendar.md)
  The calendar for the calendar item.
- [var title: String!](./title.md)
  The title for the calendar item.
- [var location: String?](./location.md)
  The location associated with the calendar item.
- [var lastModifiedDate: Date?](./lastmodifieddate.md)
  The date that the calendar item was last modified.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone for the calendar item.
- [var url: URL?](./url.md)
  The URL for the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/creationdate)*