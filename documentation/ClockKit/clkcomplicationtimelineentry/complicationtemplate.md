# complicationTemplate

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The template containing the data to display in your complication.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var complicationTemplate: CLKComplicationTemplate { get set }
```

```objc
@property (nonatomic, copy) CLKComplicationTemplate * complicationTemplate;
```

#### Discussion

Specify a template that matches the style of complication for which you’re providing data. Different templates require different types of data. You must configure the template data before returning the timeline entry to ClockKit.

## See Also

### Setting the Entry Values
- [var date: Date](./date.md)
  The time at which to display the entry.
- [var timelineAnimationGroup: String?](./timelineanimationgroup.md)
  The animation group to which the entry belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/complicationtemplate)*