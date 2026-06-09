# init(resolvedType:confidence:strategyUsed:)

**Framework**: Core Spotlight  
**Kind**: init

Create a UTType resolution result with minimal parameters

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(resolvedType: String, confidence: Double, strategyUsed: String)
```

#### Discussion

Convenience initializer for simple cases without path tracking or metadata.

## Parameters

- `resolvedType`: The resolved UTType identifier (must not be empty)
- `confidence`: Confidence level (will be clamped to [0.0, 1.0])
- `strategyUsed`: Strategy name (must not be empty)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/uttyperesolutionresult/init(resolvedtype:confidence:strategyused:))*