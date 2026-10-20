# unitStyle

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The preferred style for units.

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
var unitStyle: MKDistanceFormatter.DistanceUnitStyle { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign) MKDistanceFormatterUnitStyle unitStyle;
```

*macOS*

```objc
@property (atomic, assign) MKDistanceFormatterUnitStyle unitStyle;
```

#### Discussion

You can abbreviate or fully spell out units. The default value of this property is [`MKDistanceFormatter.DistanceUnitStyle.default`](./distanceunitstyle/default.md), which bases the style on the user’s locale and language settings.

## See Also

### Specifying the format
- [var locale: Locale!](./locale.md)
  The locale to use when formatting strings.
- [var units: MKDistanceFormatter.Units](./units-swift.property.md)
  The measuring system — imperial or metric — to use for units.
- [MKDistanceFormatter.Units](./units-swift.enum.md)
  Constants that reflect the type of units to use in the string.
- [MKDistanceFormatter.DistanceUnitStyle](./distanceunitstyle.md)
  Constants that indicate the format style to use for strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle)*