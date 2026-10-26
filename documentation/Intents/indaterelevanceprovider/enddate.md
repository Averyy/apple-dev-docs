# endDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The relevant end date.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var endDate: Date? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * endDate;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDate * endDate;
```

#### Discussion

If the end date isn’t specified when creating the [`INDateRelevanceProvider`](../indaterelevanceprovider.md) object, this property is `nil`.

## See Also

### Getting the Relevant Dates
- [var startDate: Date](./startdate.md)
  The relevant start date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indaterelevanceprovider/enddate)*