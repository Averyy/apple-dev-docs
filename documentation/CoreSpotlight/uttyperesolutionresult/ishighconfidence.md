# isHighConfidence

**Framework**: Core Spotlight  
**Kind**: property

Whether this resolution has high confidence (>0.8)

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var isHighConfidence: Bool { get }
```

#### Discussion

Use this to filter out low-confidence results that may require fallback or validation.

**Example:**

```swift
let results = strategies.compactMap { try? await $0.resolve(type) }
let highConfidenceResults = results.filter { $0.isHighConfidence }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/uttyperesolutionresult/ishighconfidence)*