---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/filemover(ispresented:files:oncompletion:oncancellation:)"
framework: "CareKit/CareKitUI"
---

# fileMover(isPresented:files:onCompletion:onCancellation:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.fileMover(isPresented:files:onCompletion:onCancellation:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: @escaping () -> Void) -> some View where C : Collection, C.Element == URL
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/filemover(ispresented:files:oncompletion:oncancellation:))*