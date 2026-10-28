# calendars

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The calendars that belong to this source object.

**Availability**:
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
var calendars: Set<EKCalendar> { get }
```

```objc
@property (nonatomic, readonly) NSSet<EKCalendar *> * calendars;
```

## Discussion

> **Note**:  This property is not available in macOS.

## See Also

### Accessing Calendars
- [func calendars(for: EKEntityType) -> Set<EKCalendar>](./calendars%28for%29.md)
  Returns the calendars that belong to this source object that support a particular entity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/eksource/calendars)*