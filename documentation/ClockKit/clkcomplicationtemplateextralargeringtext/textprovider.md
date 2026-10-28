# textProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The text to display in the complication.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var textProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * textProvider;
```

## Discussion

Space for text is limited in this particular template so keep strings as short as possible.

## See Also

### Setting the Complication Data
- [var fillFraction: Float](./fillfraction.md)
  Setting the Complication Data.
- [var ringStyle: CLKComplicationRingStyle](./ringstyle.md)
  The style of the progress ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext/textprovider)*