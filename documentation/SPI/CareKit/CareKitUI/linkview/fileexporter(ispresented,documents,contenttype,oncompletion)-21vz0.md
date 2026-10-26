---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/fileexporter(ispresented:documents:contenttype:oncompletion:)-21vz0"
framework: "CareKit/CareKitUI"
---

# fileExporter(isPresented:documents:contentType:onCompletion:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.fileExporter(isPresented:documents:contentType:onCompletion:)`.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: @escaping (Result<[URL], any Error>) -> Void) -> some View where C : Collection, C.Element : FileDocument
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/fileexporter(ispresented:documents:contenttype:oncompletion:)-21vz0)*