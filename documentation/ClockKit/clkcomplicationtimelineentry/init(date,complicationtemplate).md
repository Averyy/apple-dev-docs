# init(date:complicationTemplate:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a timeline entry with the specified date and complication data.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(date: Date, complicationTemplate: CLKComplicationTemplate)
```

```objc
+ (instancetype) entryWithDate:(NSDate *) date complicationTemplate:(CLKComplicationTemplate *) complicationTemplate;
```

#### Return Value

A timeline entry initialized with the specified data.

#### Discussion

Use this method to create new timeline entries. You can change the values of the timeline entry later by modifying the properties of the returned object. This method sets the value of the [`timelineAnimationGroup`](./timelineanimationgroup.md) property to `nil`.

## Parameters

- `date`: The time at which to display the complication data.
- `complicationTemplate`: The complication template containing the data to display. The template must belong to the family of the associated complication.

## See Also

### Creating a Timeline Entry
- [convenience init(date: Date, complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup: String?)](./init%28date,complicationtemplate,timelineanimationgroup%29.md)
  Creates and returns a timeline entry with the specified information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/init(date:complicationtemplate:))*