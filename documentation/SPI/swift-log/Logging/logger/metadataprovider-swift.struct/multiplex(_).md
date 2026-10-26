---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadataprovider-swift.struct/multiplex(_:)"
framework: "swift-log/Logging"
---

# multiplex(_:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Type Method

A pseudo metadata provider that merges metadata from multiple other metadata providers.

## Declaration

```swift
static func multiplex(_ providers: [Logger.MetadataProvider]) -> Logger.MetadataProvider?
```

#### Return Value

A pseudo-`MetadataProvider` merging metadata from the given `MetadataProvider`s.

##### Merging conflicting keys

`MetadataProvider`s are invoked left to right in the order specified in the `providers` argument. In case multiple providers try to add a value for the same key, the last provider “wins” and its value is being used.

## Parameters

- `providers`: An array of `MetadataProvider`s to delegate to. The array must not be empty.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadataprovider-swift.struct/multiplex(_:))*