# searchTermsOperator

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The operator that defines how to incorporate the search terms when performing the search.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var searchTermsOperator: INConditionalOperator { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INConditionalOperator searchTermsOperator;
```

*macOS*

```objc
@property (atomic, assign, readonly) INConditionalOperator searchTermsOperator;
```

#### Discussion

This property indicates whether photos must contain all, some, or none of the terms listed in the [`searchTerms`](./searchterms.md) property.

## See Also

### Getting the Search Terms
- [var searchTerms: [String]?](./searchterms.md)
  An array of terms to look for in the photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintent/searchtermsoperator)*