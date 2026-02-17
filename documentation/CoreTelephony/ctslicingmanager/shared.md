# shared

**Framework**: Core Telephony  
**Kind**: property

A shared singleton instance for accessing network slicing functionality.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
static let shared: CTSlicingManager
```

#### Discussion

Use this shared instance to access all network slicing capabilities. The `CTSlicingManager` uses a singleton pattern to ensure consistent state management across your app.

```swift
let manager = CTSlicingManager.shared
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/shared)*