# dateTimeRange

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The range of dates in which to search for messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var dateTimeRange: INDateComponentsRange? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INDateComponentsRange * dateTimeRange;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INDateComponentsRange * dateTimeRange;
```

## Discussion

Use this property to limit the scope of the search to sent or received messages within the specified dates.

## See Also

### Getting the Search Criteria
- [var searchTerms: [String]?](./searchterms.md)
  The terms to look for in the messages.
- [var searchTermsOperator: INConditionalOperator](./searchtermsoperator.md)
  The operator that defines how to use the set of terms in the search criteria.
- [var attributes: INMessageAttributeOptions](./attributes.md)
  The attributes that must be present on a message to yield a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/datetimerange)*