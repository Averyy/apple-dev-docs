---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkittask/init(id:title:careplanuuid:schedule:healthkitlinkage:)"
framework: "CareKit/CareKitStore"
---

# init(id:title:carePlanUUID:schedule:healthKitLinkage:)

**Framework**: CareKit/CareKitStore  
**Kind**: init  
**Role**: Initializer

Instantiate a new `OCKHealthKitTask`

## Declaration

```swift
init(id: String, title: String?, carePlanUUID: UUID?, schedule: OCKSchedule, healthKitLinkage: OCKHealthKitLinkage)
```

## Parameters

- `id`: A unique id for this HealthKit task chosen by the developer.
- `title`: A title that will be used to represent this HealthKit task to the patient.
- `carePlanUUID`: The UUID of the care plan that this task belongs to.
- `schedule`: A schedule specifying when this task is to be completed.
- `healthKitLinkage`: A structure specifying how this task is linked with HealthKit.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkittask/init(id:title:careplanuuid:schedule:healthkitlinkage:))*