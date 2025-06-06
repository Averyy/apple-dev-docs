# query(_:foundResults:error:)

**Framework**: Open Directory  
**Kind**: method  
**Required**: Yes

The delegate method called as results are returned from a query scheduled in a run loop.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func query(_ inQuery: ODQuery!, foundResults inResults: [Any]!, error inError: (any Error)!)
```

#### Discussion

This method is called as soon as any results become available. Results must be retained or copied. If both `inResults` and `inError` are `nil`, the query has completed.

## Parameters

- `inQuery`: The query.
- `inResults`: Partial results returned from the query.
- `inError`: An error reference for error details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquerydelegate/query(_:foundresults:error:))*