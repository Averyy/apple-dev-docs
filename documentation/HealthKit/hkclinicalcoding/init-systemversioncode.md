# init(system:version:code:)

**Framework**: HealthKit  
**Kind**: init

Creates a clinical coding with the specified system, version, and code.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(system: String, version: String?, code: String)
```

#### Discussion

Use when you need to explicitly construct a coding object to associate a HealthKit concept with a standardized medical code.

## Parameters

- `system`: The string that identifies the coding system, typically a HL7 URL.
- `version`: The version of the system, if applicable.
- `code`: The clinical code string that represents the medical concept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicalcoding/init(system:version:code:))*