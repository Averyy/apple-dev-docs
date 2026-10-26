---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockremotesynchronizable/chooseconflictresolution(conflicts:completion:)"
framework: "CareKit/CareKitStore"
---

# chooseConflictResolution(conflicts:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

This method will be called when CareKit detects a conflict between changes made to an entity in the device’s local store and the changes made to the same entity in other device’s stores. Inspect the conflicted and determine which version of the entity to keep, then call the completion closure with the chosen version.

## Declaration

```swift
func chooseConflictResolution(conflicts: [OCKEntity], completion: @escaping OCKResultClosure<OCKEntity>)
```

#### Discussion

> **Note**: It is permissible to decide for the user, or to prompt the user to make a selection manually.

## Parameters

- `conflicts`: An array of the entities that are in conflict.
- `completion`: A closure that should be called with the version to keep.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockremotesynchronizable/chooseconflictresolution(conflicts:completion:))*