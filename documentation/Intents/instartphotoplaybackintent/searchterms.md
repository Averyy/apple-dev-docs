# searchTerms

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of terms to look for in the photos.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var searchTerms: [String]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSString *> * searchTerms;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<NSString *> * searchTerms;
```

#### Discussion

When this property contains one or more [`NSString`](../../Foundation/nsstring.md) objects, your search should return only photos whose tags, keywords, descriptions, or other attributes contain one of the specified strings. Use the value of the [`searchTermsOperator`](./searchtermsoperator.md) property to determine whether the search should be for all, some, or none of the specified terms.

## See Also

### Getting the Search Terms
- [var searchTermsOperator: INConditionalOperator](./searchtermsoperator.md)
  The operator that defines how to incorporate the search terms when performing the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintent/searchterms)*