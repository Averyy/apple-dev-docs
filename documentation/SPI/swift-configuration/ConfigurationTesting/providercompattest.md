---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configurationtesting/providercompattest"
framework: "swift-configuration/ConfigurationTesting"
---

# ProviderCompatTest

**Framework**: swift-configuration/ConfigurationTesting  
**Kind**: struct  
**Role**: Structure

A comprehensive test suite for validating `ConfigProvider` implementations.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ProviderCompatTest
```

#### Overview

This test suite verifies that configuration providers correctly implement all required functionality including synchronous and asynchronous value retrieval, snapshot operations, and value watching capabilities.

#### Usage

Create a test instance with your provider and run the compatibility tests:

```swift
let provider = MyCustomProvider()
let test = ProviderCompatTest(provider: provider)
try await test.runTest()
```

#### Required Test Data

The provider under test must be populated with specific test values to ensure comprehensive validation. The required configuration data includes:

```swift
[
    "string": String("Hello"),
    "other.string": String("Other Hello"),
    "int": Int(42),
    "other.int": Int(24),
    "double": Double(3.14),
    "other.double": Double(2.72),
    "bool": Bool(true),
    "other.bool": Bool(false),
    "bytes": [UInt8](.magic),
    "other.bytes": [UInt8](.magic2),
    "stringy.array": [String](["Hello", "World"]),
    "other.stringy.array": [String](["Hello", "Swift"]),
    "inty.array": [Int]([42, 24]),
    "other.inty.array": [Int]([16, 32]),
    "doubly.array": [Double]([3.14, 2.72]),
    "other.doubly.array": [Double]([0.9, 1.8]),
    "booly.array": [Bool]([true, false]),
    "other.booly.array": [Bool]([false, true, true]),
    "byteChunky.array": [[UInt8]]([.magic, .magic2]),
    "other.byteChunky.array": [[UInt8]]([.magic, .magic2, .magic]),
]
```

## Topics

### Structures
- [ProviderCompatTest.TestConfiguration](./providercompattest/testconfiguration.md)
  Configuration options for customizing test behavior.
### Initializers
- [init(provider: any ConfigProvider, configuration: ProviderCompatTest.TestConfiguration)](./providercompattest/init%28provider,configuration%29.md)
  Creates a new compatibility test suite.
### Instance Methods
- [func runTest() async throws](./providercompattest/runtest%28%29.md)
  Executes the complete compatibility test suite.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configurationtesting/providercompattest)*