# init(date:complicationTemplate:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns a timeline entry with the specified date and complication data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(date: Date, complicationTemplate: CLKComplicationTemplate)
```

#### Return Value

A timeline entry initialized with the specified data.

#### Discussion

Use this method to create new timeline entries. You can change the values of the timeline entry later by modifying the properties of the returned object. This method sets the value of the [`timelineAnimationGroup`](clkcomplicationtimelineentry/timelineanimationgroup.md) property to `nil`.

## Parameters

- `date`: The time at which to display the complication data.
- `complicationTemplate`: The complication template containing the data to display. The template must belong to the family of the associated complication.

## See Also

- [convenience init(date: Date, complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup: String?)](clkcomplicationtimelineentry/init(date:complicationtemplate:timelineanimationgroup:).md)
  Creates and returns a timeline entry with the specified information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/init(date:complicationtemplate:))*