# UTTypeResolutionStrategy

**Framework**: Core Spotlight  
**Kind**: protocol

Protocol for pluggable UTType resolution strategies

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol UTTypeResolutionStrategy
```

#### Overview

Implement this protocol to provide different approaches to resolving UTTypes in the hierarchy. Strategies are composable - multiple strategies can be tried in sequence until one succeeds.

**Strategy Contract:**

- Return `nil` if the strategy cannot resolve the type (normal case - try another strategy)
- Return `UTTypeResolutionResult` if resolution succeeds
- Throw an error only for critical failures (network errors, invalid input format, etc.)

**Example Implementation:**

```swift
struct HierarchyStrategy: UTTypeResolutionStrategy {
    var name: String { "hierarchy" }

    func resolve(_ originalType: String) async throws -> UTTypeResolutionResult? {
        guard let uttype = UTType(originalType) else {
            return nil  // Cannot handle this type
        }

        var path: [String] = [originalType]
        var current = uttype

        while let supertype = current.supertype {
            path.append(supertype.identifier)
            current = supertype
        }

        return UTTypeResolutionResult(
            resolvedType: path.last ?? originalType,
            confidence: 1.0,
            strategyUsed: name,
            resolutionPath: path
        )
    }
}
```

**When to Return vs Throw:**

- Return `nil`: “I don’t know how to resolve this type” (normal)
- Throw error: “Something went wrong during resolution” (exceptional)

## Topics

### Instance Properties
- [var name: String](uttyperesolutionstrategy/name.md)
  Unique identifier for this resolution strategy
### Instance Methods
- [func resolve(String) async throws -> UTTypeResolutionResult?](uttyperesolutionstrategy/resolve(_:).md)
  Attempt to resolve a UTType identifier

## Relationships

### Conforming Types
- [UTTypeHierarchyStrategy](uttypehierarchystrategy.md)

## See Also

- [class UTTypeHierarchyStrategy](uttypehierarchystrategy.md)
  Strategy for resolving UTTypes by walking the LaunchServices type hierarchy using BFS traversal
- [struct UTTypeResolutionResult](uttyperesolutionresult.md)
  Result of a UTType resolution operation with confidence metrics and context


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/uttyperesolutionstrategy)*