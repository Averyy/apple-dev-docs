# init(tollAmount:locale:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for a toll amount.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(tollAmount value: Double, locale: Locale)
```

#### Return Value

A new @c CPRouteDetail instance representing the toll amount

#### Discussion

Use this method to display toll costs associated with a route. The toll amount will be formatted according to the provided locale’s currency settings.

Toll information helps users make informed routing decisions, particularly when comparing routes with varying toll costs. The system automatically formats the value using the locale’s currency symbol, decimal separator, and digit grouping conventions.

> **Note**: The system displays toll amounts with high visibility during route selection to help users understand cost implications before committing to a route.

## Parameters

- `value`: The toll amount as a decimal value (e.g., 5.50 for $5.50)
- `locale`: The locale to use for currency formatting. The locale’s currency code determines the currency symbol and formatting rules. Pass @c [NSLocale currentLocale] to use the user’s preferred locale, or create a specific locale for fixed currency display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(tollamount:locale:))*