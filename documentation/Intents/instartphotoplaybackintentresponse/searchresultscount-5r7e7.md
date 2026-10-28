# searchResultsCount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The number of photos that match the search parameters.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 10.0+ - Deprecated in 15.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@nonobjc
final var searchResultsCount: Int? { get set }
```

## Discussion

Use this property to specify the number of photos found during the search. Typically, you assign a value to this property only after handling the intent. During the confirmation phase, you can set the value of this property set to `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintentresponse/searchresultscount-5r7e7)*