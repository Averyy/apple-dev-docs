# init(resolvedType:confidence:strategyUsed:resolutionPath:metadata:)

**Framework**: Core Spotlight  
**Kind**: init

Create a UTType resolution result with full parameters

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(resolvedType: String, confidence: Double, strategyUsed: String, resolutionPath: [String], metadata: [String : Any] = [:])
```

#### Discussion

> **Note**: Confidence values outside [0.0, 1.0] are automatically clamped

> **Note**: Empty resolvedType or strategyUsed will trigger assertion in debug builds

## Parameters

- `resolvedType`: The resolved UTType identifier (must not be empty)
- `confidence`: Confidence level (will be clamped to [0.0, 1.0])
- `strategyUsed`: Strategy name (must not be empty)
- `resolutionPath`: Hierarchy path taken during resolution
- `metadata`: Additional context (default: empty dictionary)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/uttyperesolutionresult/init(resolvedtype:confidence:strategyused:resolutionpath:metadata:))*