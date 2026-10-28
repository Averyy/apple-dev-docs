# Locale.Components

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents the components of a locale, for use when creating a locale with specific overrides.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Components
```

## Overview

Use [`Locale.Components`](./components.md) with the [`init(components:)`](./init%28components%29.md) initializer to create a custom [`Locale`](../locale.md) that overrides specific traits of a default locale. When you create a locale with components, the locale uses any overridden values instead of defaults preferred by the region or language. Leave a property `nil` to accept the default value.

The properties in this type correspond with those in [`Locale`](../locale.md), which declares them as read-only rather than read-write. You use this type to customize components when creating a custom locale, and use [`Locale`](../locale.md) to examine the components of an existing locale.

The following example creates a [`Locale.Components`](./components.md) instance for US English, but then customizes its components. It sets the first day of the week to Monday and the hour cycle to zero-to-23. These components override the `en-US` defaults of Sunday and one-to-12, respectively. It then uses [`init(components:)`](./init%28components%29.md) to create a custom [`Locale`](../locale.md).

```swift
var components = Locale.Components(languageCode: "en", languageRegion: "US")
components.firstDayOfWeek = Locale.Weekday.monday
components.hourCycle = Locale.HourCycle.zeroToTwentyThree
let locale = Locale(components: components)
```

## Topics

### Creating a locale components instance
- [init(identifier: String)](./components/init%28identifier%29.md)
  Creates a locale components instance with the specified identifier.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, languageRegion: Locale.Region?)](./components/init%28languagecode,script,languageregion%29.md)
  Creates a locale components instance with the specified language code, script, and region identifier.
- [init(locale: Locale)](./components/init%28locale%29.md)
  Creates a language components instance from an existing locale.
### Specifying language components
- [var languageComponents: Locale.Language.Components](./components/languagecomponents.md)
  The Unicode language identifier part of a locale.
- [Locale.Language.Components](./language-swift.struct/components.md)
  A type that identifies a language by its various components.
### Specifying date and time components
- [var calendar: Calendar.Identifier?](./components/calendar.md)
  The calendar used by the locale.
- [Calendar.Identifier](../calendar/identifier-swift.enum.md)
  An enumeration for the available calendars.
- [var firstDayOfWeek: Locale.Weekday?](./components/firstdayofweek.md)
  The first day of the week as represented by this locale.
- [Locale.Weekday](./weekday.md)
  A type that represents weekdays, used for indicating a locale’s first day of the week.
- [var hourCycle: Locale.HourCycle?](./components/hourcycle.md)
  The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.
- [Locale.HourCycle](./hourcycle-swift.enum.md)
  A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
- [var timeZone: TimeZone?](./components/timezone.md)
  The time zone used by the locale.
### Specifiying measurement and counting components
- [var currency: Locale.Currency?](./components/currency.md)
  The currency used by the locale.
- [Locale.Currency](./currency-swift.struct.md)
  A type that represents the currency system used by a locale, like dollars or euros.
- [var measurementSystem: Locale.MeasurementSystem?](./components/measurementsystem.md)
  The measurement system used by the locale, like metric or the US system.
- [Locale.MeasurementSystem](./measurementsystem-swift.struct.md)
  A type that represents the measurement system used by a locale, like metric or the US system.
- [var numberingSystem: Locale.NumberingSystem?](./components/numberingsystem.md)
  The numbering system used by the locale.
- [Locale.NumberingSystem](./numberingsystem-swift.struct.md)
  A type that represents the numbering system used in a locale.
### Specifying region components
- [var region: Locale.Region?](./components/region.md)
  The region used by the locale.
- [Locale.Region](./region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var subdivision: Locale.Subdivision?](./components/subdivision.md)
  The optional subdivision of the region used by this locale.
- [Locale.Subdivision](./subdivision-swift.struct.md)
  A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [var variant: Locale.Variant?](./components/variant.md)
  An optional variant used by the locale.
- [Locale.Variant](./variant-swift.struct.md)
  A type that represents a locale’s language variant.
### Specifying ordering components
- [var collation: Locale.Collation?](./components/collation.md)
  The string sort order of the locale.
- [Locale.Collation](./collation-swift.struct.md)
  A type that represents the string sort order used by the locale.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a locale by components
- [init(components: Locale.Components)](./init%28components%29.md)
  Creates a locale from the given components.
- [init(languageCode: Locale.LanguageCode?, script: Locale.Script?, languageRegion: Locale.Region?)](./init%28languagecode,script,languageregion%29.md)
  Creates a locale with the specified language code, script, and region identifier.
- [init(languageComponents: Locale.Language.Components)](./init%28languagecomponents%29.md)
  Creates a locale from the given language components.
- [Locale.Language.Components](./language-swift.struct/components.md)
  A type that identifies a language by its various components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/components)*