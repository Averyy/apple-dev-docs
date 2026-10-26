---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attach(patientstore:)"
framework: "CareKit/CareKitStore"
---

# attach(patientStore:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Attaches a new store. The new store must be capable of reading and writing patients.

## Declaration

```swift
func attach(patientStore: OCKAnyPatientStore)
```

#### Discussion

> **Note**: The order is which stores are attached is important.

> **See Also**: `OCKStoreCoordinator`

## Parameters

- `patientStore`: Any store that conforms to `OCKAnyPatientStore`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attach(patientstore:))*