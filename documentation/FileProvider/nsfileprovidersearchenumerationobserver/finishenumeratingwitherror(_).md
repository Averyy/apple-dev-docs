# finishEnumeratingWithError(_:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Finishes a search enumeration by sending an error to the framework.

**Availability**:
- macOS 26.0+

## Declaration

```swift
func finishEnumeratingWithError(_ error: any Error)
```

```objc
- (void) finishEnumeratingWithError:(NSError *) error;
```

#### Discussion

Finishing with an error causes the system to stop requesting additional pages of results. The system doesn’t retry after you call this method. If an error is potentially recoverable, you can perform your own retry in your implementation of [`enumerateSearchResults(for:startingAt:)`](../nsfileprovidersearchenumerator/enumeratesearchresults%28for,startingat%29.md) and continue if successful, or end the query by calling this method.

## See Also

### Ending enumeration
- [func finishEnumerating(upTo: NSFileProviderPage?)](./finishenumerating%28upto%29.md)
  Finish enumerating a page of results, and optionally provide a location within the results to continue the enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerationobserver/finishenumeratingwitherror(_:))*