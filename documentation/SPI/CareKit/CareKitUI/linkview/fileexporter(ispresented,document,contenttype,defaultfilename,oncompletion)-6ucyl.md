---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-6ucyl"
framework: "CareKit/CareKitUI"
---

# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)`.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void) -> some View where D : FileDocument
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-6ucyl)*