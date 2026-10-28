# searchTermsOperator

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The operator that defines how to use the set of terms in the search criteria.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

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

## Discussion

This property indicates whether the message must contain all, some, or none of the terms listed in the [`searchTerms`](./searchterms.md) property.

## See Also

### Getting the Search Criteria
- [var searchTerms: [String]?](./searchterms.md)
  The terms to look for in the messages.
- [var dateTimeRange: INDateComponentsRange?](./datetimerange.md)
  The range of dates in which to search for messages.
- [var attributes: INMessageAttributeOptions](./attributes.md)
  The attributes that must be present on a message to yield a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/searchtermsoperator)*