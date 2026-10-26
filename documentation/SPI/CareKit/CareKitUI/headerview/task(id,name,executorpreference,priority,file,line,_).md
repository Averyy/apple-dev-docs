---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/task(id:name:executorpreference:priority:file:line:_:)"
framework: "CareKit/CareKitUI"
---

# task(id:name:executorPreference:priority:file:line:_:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.task(id:name:executorPreference:priority:file:line:_:)`.

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
func task<T>(id: T, name: String? = nil, executorPreference taskExecutor: any TaskExecutor, priority: TaskPriority = .userInitiated, file: String = #fileID, line: Int = #line, _ action: sending @escaping @isolated(any) () async -> Void) -> some View where T : Equatable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/task(id:name:executorpreference:priority:file:line:_:))*