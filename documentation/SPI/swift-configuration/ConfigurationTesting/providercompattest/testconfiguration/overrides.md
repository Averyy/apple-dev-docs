---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configurationtesting/providercompattest/testconfiguration/overrides"
framework: "swift-configuration/ConfigurationTesting"
---

# overrides

**Framework**: swift-configuration/ConfigurationTesting  
**Kind**: property  
**Role**: Instance Property

Value overrides for testing custom scenarios.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var overrides: [String : ConfigContent]
```

#### Discussion

Use this to test how your provider handles different values than the standard test dataset. Keys should match the dot-separated format used in the test data.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configurationtesting/providercompattest/testconfiguration/overrides)*