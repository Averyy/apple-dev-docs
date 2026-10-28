# enumeratorForChangeHistoryFetchRequest:error:

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Enumerates a change history fetch request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (CNFetchResult<NSEnumerator<CNChangeHistoryEvent *> *> *) enumeratorForChangeHistoryFetchRequest:(CNChangeHistoryFetchRequest *) request error:(NSError **) error;
```

## Return Value

An enumerator of the events matching the result, or `nil` if there was an error.

## Discussion

Executes the fetch request and returns an enumerator for the results. This can prevent all events from loading into memory at once. An error that occurs during enumeration may throw an exception.

## Parameters

- `request`: A description of the events to fetch.
- `error`: If the fetch fails, contains an [`NSError`](../../Foundation/nserror.md) object with more information.

## See Also

### Fetching change history info
- [var currentHistoryToken: Data?](./currenthistorytoken.md)
  The current history token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/enumeratorforchangehistoryfetchrequest:error:)*