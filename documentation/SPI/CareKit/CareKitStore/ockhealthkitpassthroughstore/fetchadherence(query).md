---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitpassthroughstore/fetchadherence(query:)"
framework: "CareKit/CareKitStore"
---

# fetchAdherence(query:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

`fetchAdherence` retrieves all the events and calculates the percent of tasks completed for every day between two dates.

## Declaration

```swift
func fetchAdherence(query: OCKAdherenceQuery) async throws -> [OCKAdherence]
```

## Discussion

The way completion is computed depends on how many `expectedValues` a task has. If it has no expected values, then having an outcome with at least one value will count as complete. If a task has expected values, completion will be computed as ratio of the number of outcome values to the number of expected values.

## Parameters

- `query`: A query used to constrain the values that will be fetched.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitpassthroughstore/fetchadherence(query:))*