# attributes

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The attributes that must be present on a message to yield a match.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var attributes: INMessageAttributeOptions { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INMessageAttributeOptions attributes;
```

*macOS*

```objc
@property (atomic, assign, readonly) INMessageAttributeOptions attributes;
```

#### Discussion

Use this property to limit the scope of the search to messages with the specified attributes.

## See Also

### Getting the Search Criteria
- [var searchTerms: [String]?](./searchterms.md)
  The terms to look for in the messages.
- [var searchTermsOperator: INConditionalOperator](./searchtermsoperator.md)
  The operator that defines how to use the set of terms in the search criteria.
- [var dateTimeRange: INDateComponentsRange?](./datetimerange.md)
  The range of dates in which to search for messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/attributes)*