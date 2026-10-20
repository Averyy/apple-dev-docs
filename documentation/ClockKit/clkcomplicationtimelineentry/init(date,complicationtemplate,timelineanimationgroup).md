# init(date:complicationTemplate:timelineAnimationGroup:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a timeline entry with the specified information.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(date: Date, complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup: String?)
```

```objc
+ (instancetype) entryWithDate:(NSDate *) date complicationTemplate:(CLKComplicationTemplate *) complicationTemplate timelineAnimationGroup:(NSString *) timelineAnimationGroup;
```

#### Return Value

A timeline entry initialized with the specified data.

#### Discussion

Use this method to create new timeline entries. You can change the values of the timeline entry later by modifying the properties of the returned object.

## Parameters

- `date`: The time at which to display the complication data.
- `complicationTemplate`: The complication template containing the data to display. Specify a template that’s appropriate for the complication family.
- `timelineAnimationGroup`: The animation group with which to associate the entry. For more information about how this value is used, see [`timelineAnimationGroup`](./timelineanimationgroup.md).

## See Also

### Creating a Timeline Entry
- [convenience init(date: Date, complicationTemplate: CLKComplicationTemplate)](./init%28date,complicationtemplate%29.md)
  Creates and returns a timeline entry with the specified date and complication data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/init(date:complicationtemplate:timelineanimationgroup:))*