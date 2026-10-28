---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshot/providername"
framework: "swift-configuration/Configuration"
---

# providerName

**Framework**: swift-configuration/Configuration  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The human-readable name of the configuration provider that created this snapshot.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var providerName: String { get }
```

## Discussion

Used by [`AccessReporter`](../accessreporter.md) and when diagnostic logging the config reader types.

## See Also

### Required methods
- [func value(forKey: AbsoluteConfigKey, type: ConfigType) throws -> LookupResult](./value%28forkey,type%29.md)
  Returns a value for the specified key from this immutable snapshot.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshot/providername)*