# searchResultsCount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The number of photos that match the search parameters.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSNumber * searchResultsCount;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSNumber * searchResultsCount;
```

#### Discussion

Use this property to specify the number of photos found during the search. Typically, you assign a value to this property only after handling the intent. During the confirmation phase, you can set the value of this property set to `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintentresponse/searchresultscount-6ns8y)*