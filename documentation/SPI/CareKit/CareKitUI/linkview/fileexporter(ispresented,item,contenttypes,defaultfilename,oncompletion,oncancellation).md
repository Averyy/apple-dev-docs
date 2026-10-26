---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:)"
framework: "CareKit/CareKitUI"
---

# fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType] = [], defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void, onCancellation: @escaping () -> Void = { }) -> some View where T : Transferable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:))*