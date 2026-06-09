# resolve(_:)

**Framework**: Core Spotlight  
**Kind**: method

Resolve UTType by walking hierarchy using BFS

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final nonisolated(nonsending) func resolve(_ originalType: String) async throws -> UTTypeResolutionResult?
```

#### Return Value

Resolution result if supported parent found, nil if UTType invalid or no supported parent

#### Discussion

Performs breadth-first traversal of the UTType hierarchy to find the first supported parent type. Handles multiple inheritance by exploring all supertypes at each level before descending.

> **Note**: Never throws - returns nil for all error cases (graceful degradation)

**Algorithm Steps:**

1. Validate UTType exists
2. Check if original type is already supported (depth 0, confidence 1.0)
3. BFS traversal of supertypes up to maxDepth levels
4. Track visited types to prevent cycles
5. Return first supported parent with confidence based on depth

**Complexity:** O(V + E) where V = types in hierarchy, E = conformance edges

## Parameters

- `originalType`: UTI to resolve (e.g., “com.apple.mail.emlx”)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/uttypehierarchystrategy/resolve(_:))*