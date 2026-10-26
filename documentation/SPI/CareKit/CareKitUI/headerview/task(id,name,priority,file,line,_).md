---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/task(id:name:priority:file:line:_:)"
framework: "CareKit/CareKitUI"
---

# task(id:name:priority:file:line:_:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.task(id:name:priority:file:line:_:)`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func task<T>(id: T, name: String? = nil, priority: TaskPriority = .userInitiated, file: String = #fileID, line: Int = #line, _ action: sending @escaping @isolated(any) () async -> Void) -> some View where T : Equatable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/task(id:name:priority:file:line:_:))*