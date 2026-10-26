---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyoutcomestore/anyoutcomes(matching:)"
framework: "CareKit/CareKitStore"
---

# anyOutcomes(matching:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A continuous stream of outcomes that exist in the store.

## Declaration

```swift
func anyOutcomes(matching query: OCKOutcomeQuery) -> CareStoreQueryResults<OCKAnyOutcome>
```

#### Discussion

The stream yields a new value whenever the result changes and yields an error if there’s an issue accessing the store or fetching results.

Supply a query that’ll be used to match outcomes in the store. If the query doesn’t contain a date interval, the result contains the latest version of each outcome. If the query does contain a date interval, the result contains outcomes whose events occur within the interval.

This method doesn’t check if an outcome’s task is effective in the query interval.

## Parameters

- `query`: Used to match outcomes in the store.

## Default Implementations

### OCKAnyReadOnlyOutcomeStore Implementations
- [func anyOutcomes(matching: OCKOutcomeQuery) -> CareStoreQueryResults<OCKAnyOutcome>](./anyoutcomes%28matching%29-jdg8.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyoutcomestore/anyoutcomes(matching:))*