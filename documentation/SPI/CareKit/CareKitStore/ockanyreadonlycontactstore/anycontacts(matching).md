---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycontactstore/anycontacts(matching:)"
framework: "CareKit/CareKitStore"
---

# anyContacts(matching:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A continuous stream of contacts that exist in the store.

## Declaration

```swift
func anyContacts(matching query: OCKContactQuery) -> CareStoreQueryResults<OCKAnyContact>
```

#### Discussion

The stream yields a new value whenever the result changes and yields an error if there’s an issue accessing the store or fetching results.

Supply a query that’ll be used to match contacts in the store. If the query doesn’t contain a date interval, the result will contain every version of a contact. Multiple versions of the same contact will have the same [`id`](../ockanycontact/id.md) but a different UUID. If the query does contain a date interval, the result will contain the newest version of a contact that exists in the interval.

## Parameters

- `query`: Used to match contacts in the store.

## Default Implementations

### OCKAnyReadOnlyContactStore Implementations
- [func anyContacts(matching: OCKContactQuery) -> CareStoreQueryResults<OCKAnyContact>](./anycontacts%28matching%29-1nejj.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycontactstore/anycontacts(matching:))*