---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/init(name:securityapplicationgroupidentifier:type:remote:)"
framework: "CareKit/CareKitStore"
---

# init(name:securityApplicationGroupIdentifier:type:remote:)

**Framework**: CareKit/CareKitStore  
**Kind**: init  
**Role**: Initializer

Initialize a new store by specifying its name and store type. Store’s with conflicting names and types must not be created.

## Declaration

```swift
init(name: String, securityApplicationGroupIdentifier: String? = nil, type: OCKCoreDataStoreType = .onDisk(), remote: OCKRemoteSynchronizable? = nil)
```

## Parameters

- `name`: A unique name for the store. It will be used for the filename if stored on disk.
- `securityApplicationGroupIdentifier`: App group identifier for a sandboxed app that shares files with other apps from the same developer. See [Adding an App To an App Group](./api-1.md).
- `type`: The type of store to be used. `.onDisk` is used by default.
- `remote`: A store synchronization endpoint.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/init(name:securityapplicationgroupidentifier:type:remote:))*