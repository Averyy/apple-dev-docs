---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-5fm5y"
framework: "CareKit/CareKitUI"
---

# fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType] = [], defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where D : ReferenceFileDocument
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-5fm5y)*