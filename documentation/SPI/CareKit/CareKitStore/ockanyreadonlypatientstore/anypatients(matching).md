---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlypatientstore/anypatients(matching:)"
framework: "CareKit/CareKitStore"
---

# anyPatients(matching:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A continuous stream of patients that exist in the store.

## Declaration

```swift
func anyPatients(matching query: OCKPatientQuery) -> CareStoreQueryResults<OCKAnyPatient>
```

#### Discussion

The stream yields a new value whenever the result changes and yields an error if there’s an issue accessing the store or fetching results.

Supply a query that’ll be used to match patients in the store. If the query doesn’t contain a date interval, the result will contain every version of a patient. Multiple versions of the same patient will have the same [`id`](../ockanypatient/id.md) but a different UUID. If the query does contain a date interval, the result will contain the newest version of a patient that exists in the interval.

## Parameters

- `query`: Used to match patients in the store.

## Default Implementations

### OCKAnyReadOnlyPatientStore Implementations
- [func anyPatients(matching: OCKPatientQuery) -> CareStoreQueryResults<OCKAnyPatient>](./anypatients%28matching%29-1cvvv.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlypatientstore/anypatients(matching:))*