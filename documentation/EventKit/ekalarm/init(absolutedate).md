# init(absoluteDate:)

**Framework**: EventKit  
**Kind**: init  
**Role**: Initializer

Creates and returns an alarm with an absolute date.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(absoluteDate date: Date)
```

```objc
+ (EKAlarm *) alarmWithAbsoluteDate:(NSDate *) date;
```

## Return Value

The created alarm.

## Parameters

- `date`: The date for the alarm.

## See Also

### Related Documentation
- [Calendar and Reminders Programming Guide](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009765)
### Creating an Alarm
- [init(relativeOffset: TimeInterval)](./init%28relativeoffset%29.md)
  Creates and returns an alarm with a relative offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/init(absolutedate:))*