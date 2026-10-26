---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-9enf7"
framework: "CareKit/CareKitUI"
---

# fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType] = [], onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where C : Collection, C.Element : ReferenceFileDocument
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-9enf7)*