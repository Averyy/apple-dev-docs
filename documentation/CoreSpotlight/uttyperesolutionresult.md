# UTTypeResolutionResult

**Framework**: Core Spotlight  
**Kind**: struct

Result of a UTType resolution operation with confidence metrics and context

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct UTTypeResolutionResult
```

#### Overview

Represents the outcome of attempting to resolve a UTType to a more general or specific type in the UTType hierarchy. Includes confidence scoring, resolution path tracking, and metadata for debugging and validation.

**Example Usage:**

```swift
let result = UTTypeResolutionResult(
    resolvedType: "public.message",
    confidence: 0.95,
    strategyUsed: "hierarchy",
    resolutionPath: ["com.apple.mail.emlx", "public.message", "public.data"],
    metadata: ["source": "UTType.supertype"]
)

if result.isHighConfidence {
    print("High confidence resolution: \(result.resolvedType)")
}
```

**Thread Safety:** Immutable struct - safe for concurrent access

## Topics

### Initializers
- [init(resolvedType: String, confidence: Double, strategyUsed: String)](uttyperesolutionresult/init(resolvedtype:confidence:strategyused:).md)
  Create a UTType resolution result with minimal parameters
- [init(resolvedType: String, confidence: Double, strategyUsed: String, resolutionPath: [String], metadata: [String : Any])](uttyperesolutionresult/init(resolvedtype:confidence:strategyused:resolutionpath:metadata:).md)
  Create a UTType resolution result with full parameters
### Instance Properties
- [let confidence: Double](uttyperesolutionresult/confidence.md)
  Confidence level in the resolution [0.0, 1.0]
- [var debugDescription: String](uttyperesolutionresult/debugdescription.md)
  Formatted description for debugging and logging
- [var isHighConfidence: Bool](uttyperesolutionresult/ishighconfidence.md)
  Whether this resolution has high confidence (>0.8)
- [let metadata: [String : Any]](uttyperesolutionresult/metadata.md)
  Additional context and metadata about the resolution
- [let resolutionPath: [String]](uttyperesolutionresult/resolutionpath.md)
  Hierarchy path taken during resolution
- [let resolvedType: String](uttyperesolutionresult/resolvedtype.md)
  The resolved UTType identifier (e.g., “public.message”, “public.data”)
- [let strategyUsed: String](uttyperesolutionresult/strategyused.md)
  Name of the resolution strategy that produced this result

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UTTypeHierarchyStrategy](uttypehierarchystrategy.md)
  Strategy for resolving UTTypes by walking the LaunchServices type hierarchy using BFS traversal
- [protocol UTTypeResolutionStrategy](uttyperesolutionstrategy.md)
  Protocol for pluggable UTType resolution strategies


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/uttyperesolutionresult)*