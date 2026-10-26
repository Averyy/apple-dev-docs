---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/task(name:executorpreference:priority:file:line:action:)"
framework: "CareKit/CareKitUI"
---

# task(name:executorPreference:priority:file:line:action:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.task(name:executorPreference:priority:file:line:action:)`.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
nonisolated
func task(name: String? = nil, executorPreference taskExecutor: any TaskExecutor, priority: TaskPriority = .userInitiated, file: String = #fileID, line: Int = #line, action: sending @escaping @isolated(any) () async -> Void) -> some View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/task(name:executorpreference:priority:file:line:action:))*