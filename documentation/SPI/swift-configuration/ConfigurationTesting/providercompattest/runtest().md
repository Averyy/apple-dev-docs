---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configurationtesting/providercompattest/runtest()"
framework: "swift-configuration/ConfigurationTesting"
---

# runTest()

**Framework**: swift-configuration/ConfigurationTesting  
**Kind**: method  
**Role**: Instance Method

Executes the complete compatibility test suite.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func runTest() async throws
```

#### Discussion

This method runs all provider compatibility tests including:

- Synchronous value retrieval (`getValue()`)
- Asynchronous value fetching (`fetchValue()`)
- Value watching capabilities (`watchValue()`)
- Snapshot operations (`getSnapshot()`)
- Snapshot watching (`watchSnapshot()`)

> **Throws**: Test failures or provider errors encountered during testing.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configurationtesting/providercompattest/runtest())*