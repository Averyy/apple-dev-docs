# searchTerms

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The terms to look for in the messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

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

When this property contains one or more [`NSString`](../../Foundation/nsstring.md) objects, your search should return only messages whose contents contain one of the specified strings. Use the operator in the [`searchTermsOperator`](./searchtermsoperator.md) property to determine whether to search for messages containing all, some, or none of the specified terms.

## See Also

### Getting the Search Criteria
- [var searchTermsOperator: INConditionalOperator](./searchtermsoperator.md)
  The operator that defines how to use the set of terms in the search criteria.
- [var dateTimeRange: INDateComponentsRange?](./datetimerange.md)
  The range of dates in which to search for messages.
- [var attributes: INMessageAttributeOptions](./attributes.md)
  The attributes that must be present on a message to yield a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/searchterms)*