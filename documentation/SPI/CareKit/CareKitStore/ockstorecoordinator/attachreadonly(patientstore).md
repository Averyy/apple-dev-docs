---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attachreadonly(patientstore:)"
framework: "CareKit/CareKitStore"
---

# attachReadOnly(patientStore:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Attaches a new store. The new store must be capable of reading patients.

## Declaration

```swift
func attachReadOnly(patientStore: OCKAnyReadOnlyPatientStore)
```

#### Discussion

> **Note**: The order is which stores are attached is important.

> **See Also**: `OCKStoreCoordinator`

## Parameters

- `patientStore`: Any store that conforms to `OCKAnyReadOnlyPatientStore`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attachreadonly(patientstore:))*