# UTTypeHierarchyStrategy

**Framework**: Core Spotlight  
**Kind**: class

Strategy for resolving UTTypes by walking the LaunchServices type hierarchy using BFS traversal

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class UTTypeHierarchyStrategy
```

#### Overview

This strategy walks the UTType conformance hierarchy (using `UTType.supertypes`) to find the first supported parent type. It uses breadth-first search (BFS) to prioritize closer ancestors and handles multiple inheritance by processing all supertypes at each level.

**Algorithm:**

- BFS traversal of UTType hierarchy via `supertypes`
- Maximum depth: 5 levels (user approved)
- Cycle detection via visited set
- Confidence decreases with depth: 1.0 → 0.85 → 0.70 → 0.55 → 0.50

**Example Hierarchy Walk:**

```None
Input: "com.apple.mail.emlx"
Level 0: com.apple.mail.emlx (check if supported)
Level 1: public.email-message (check if supported) ← FOUND
Return: UTTypeResolutionResult(
  resolvedType: "public.email-message",
  confidence: 0.85,
  strategyUsed: "hierarchy",
  resolutionPath: ["com.apple.mail.emlx", "public.email-message"]
)
```

**Performance:**

- Target: <30ms for typical hierarchies
- Queue-based BFS (not recursive - avoids stack overflow)
- Early termination on first supported type found

**Thread Safety:** Safe for concurrent use (immutable after init)

## Topics

### Instance Properties
- [let name: String](uttypehierarchystrategy/name.md)
  Strategy name for identification
### Instance Methods
- [func resolve(String) async throws -> UTTypeResolutionResult?](uttypehierarchystrategy/resolve(_:).md)
  Resolve UTType by walking hierarchy using BFS

## Relationships

### Conforms To
- [UTTypeResolutionStrategy](uttyperesolutionstrategy.md)

## See Also

- [struct UTTypeResolutionResult](uttyperesolutionresult.md)
  Result of a UTType resolution operation with confidence metrics and context
- [protocol UTTypeResolutionStrategy](uttyperesolutionstrategy.md)
  Protocol for pluggable UTType resolution strategies


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/uttypehierarchystrategy)*