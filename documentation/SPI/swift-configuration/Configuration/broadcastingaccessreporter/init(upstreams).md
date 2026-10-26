---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/broadcastingaccessreporter/init(upstreams:)"
framework: "swift-configuration/Configuration"
---

# init(upstreams:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new broadcasting access reporter.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(upstreams: [any AccessReporter])
```

#### Discussion

> **Precondition**: `upstreams` must not be empty.

## Parameters

- `upstreams`: The reporters that will receive forwarded events.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/broadcastingaccessreporter/init(upstreams:))*