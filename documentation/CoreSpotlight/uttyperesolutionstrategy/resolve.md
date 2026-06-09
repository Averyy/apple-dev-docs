# resolve(_:)

**Framework**: Core Spotlight  
**Kind**: method  
**Required**: Yes

Attempt to resolve a UTType identifier

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func resolve(_ originalType: String) async throws -> UTTypeResolutionResult?
```

#### Return Value

Resolution result if successful, `nil` if strategy cannot handle this type

#### Discussion

> **Note**: Only for critical errors (network failure, invalid input format, etc.)

**Implementation Guidelines:**

- Validate input format before attempting resolution
- Return `nil` for types outside strategy’s domain
- Populate resolution path for debugging
- Set appropriate confidence based on resolution method
- Include relevant metadata for downstream validation

## Parameters

- `originalType`: The UTType identifier to resolve (e.g., “com.apple.mail.emlx”)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/uttyperesolutionstrategy/resolve(_:))*