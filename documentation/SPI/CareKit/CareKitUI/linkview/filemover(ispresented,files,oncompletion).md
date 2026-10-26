---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/filemover(ispresented:files:oncompletion:)"
framework: "CareKit/CareKitUI"
---

# fileMover(isPresented:files:onCompletion:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.fileMover(isPresented:files:onCompletion:)`.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: @escaping (Result<[URL], any Error>) -> Void) -> some View where C : Collection, C.Element == URL
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/filemover(ispresented:files:oncompletion:))*