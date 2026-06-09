# debugDescription

**Framework**: Core Spotlight  
**Kind**: property

Formatted description for debugging and logging

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var debugDescription: String { get }
```

#### Discussion

Provides multi-line human-readable output showing all resolution details.

**Example Output:**

```None
UTTypeResolutionResult:
  Resolved Type: public.message
  Confidence: 0.95 (high)
  Strategy: hierarchy
  Path: com.apple.mail.emlx -> public.message -> public.data
  Metadata: {source: UTType.supertype, depth: 2}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/uttyperesolutionresult/debugdescription)*