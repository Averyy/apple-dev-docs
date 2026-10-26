# CLKAllComplicationFamilies

**Framework**: ClockKit  
**Kind**: func  
**Role**: Function

Returns an array containing all possible values of the complication family enumeration.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```c
extern NSArray<NSNumber *> *CLKAllComplicationFamilies();
```

## Mentions

- [Declaring complications for your app](./declaring-complications-for-your-app.md)

## See Also

### Migration Support
- [Migrating ClockKit complications to WidgetKit](../WidgetKit/converting-a-clockkit-app.md)
  Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
- [protocol CLKComplicationDataSource](./clkcomplicationdatasource.md)
  A protocol that provides ClockKit with information about your complication.
- [let CLKDefaultComplicationIdentifier: String](./clkdefaultcomplicationidentifier.md)
  An identifier representing a default complication.
- [class CLKComplicationDescriptor](./clkcomplicationdescriptor.md)
  A descriptor that defines a complication and the families that it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkallcomplicationfamilies)*