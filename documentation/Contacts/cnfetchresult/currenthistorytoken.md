# currentHistoryToken

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

An opaque token that indicates a point in history in the user’s Contacts database.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var currentHistoryToken: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * currentHistoryToken;
```

## Discussion

Save this token after a successful change history fetch result in your app. Then, set the saved token in [`startingToken`](../cnchangehistoryfetchrequest/startingtoken.md) in a subsequent [`CNChangeHistoryFetchRequest`](../cnchangehistoryfetchrequest.md) to receive changes after that point in history.

## See Also

### Accessing results
- [var value: ValueType](./value.md)
  The result of the fetch request, expressed as the value type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnfetchresult/currenthistorytoken)*