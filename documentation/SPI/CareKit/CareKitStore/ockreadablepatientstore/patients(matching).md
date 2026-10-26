---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore/patients(matching:)"
framework: "CareKit/CareKitStore"
---

# patients(matching:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A continuous stream of patients that exist in the store.

## Declaration

```swift
func patients(matching query: OCKPatientQuery) -> Patients
```

#### Discussion

The stream yields a new value whenever the result changes and yields an error if there’s an issue accessing the store or fetching results.

Supply a query that’ll be used to match patients in the store. If the query doesn’t contain a date interval, the result will contain every version of a patient. Multiple versions of the same patient will have the same [`id`](../ockanypatient/id.md) but a different UUID. If the query does contain a date interval, the result will contain the newest version of a patient that exists in the interval.

## Parameters

- `query`: Used to match patients in the store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore/patients(matching:))*