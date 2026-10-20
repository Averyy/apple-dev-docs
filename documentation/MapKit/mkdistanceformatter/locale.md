# locale

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The locale to use when formatting strings.

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
var locale: Locale! { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, null_resettable) NSLocale * locale;
```

*macOS*

```objc
@property (atomic, copy, null_resettable) NSLocale * locale;
```

#### Discussion

If you don’t specify an explicit locale, the formatter uses the user’s current locale information.

## See Also

### Specifying the format
- [var units: MKDistanceFormatter.Units](./units-swift.property.md)
  The measuring system — imperial or metric — to use for units.
- [MKDistanceFormatter.Units](./units-swift.enum.md)
  Constants that reflect the type of units to use in the string.
- [var unitStyle: MKDistanceFormatter.DistanceUnitStyle](./unitstyle.md)
  The preferred style for units.
- [MKDistanceFormatter.DistanceUnitStyle](./distanceunitstyle.md)
  Constants that indicate the format style to use for strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/locale)*