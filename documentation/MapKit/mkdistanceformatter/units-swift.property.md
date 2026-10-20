# units

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The measuring system — imperial or metric — to use for units.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var units: MKDistanceFormatter.Units { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign) MKDistanceFormatterUnits units;
```

*macOS*

```objc
@property (atomic, assign) MKDistanceFormatterUnits units;
```

#### Discussion

You can use this property to explicitly set the measuring system for units. The default value of this property is [`MKDistanceFormatter.Units.default`](./units-swift.enum/default.md), which bases the measuring system on the user’s locale.

## See Also

### Specifying the format
- [var locale: Locale!](./locale.md)
  The locale to use when formatting strings.
- [MKDistanceFormatter.Units](./units-swift.enum.md)
  Constants that reflect the type of units to use in the string.
- [var unitStyle: MKDistanceFormatter.DistanceUnitStyle](./unitstyle.md)
  The preferred style for units.
- [MKDistanceFormatter.DistanceUnitStyle](./distanceunitstyle.md)
  Constants that indicate the format style to use for strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/units-swift.property)*