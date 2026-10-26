---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:oncancellation:)"
framework: "CareKit/CareKitUI"
---

# fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: @escaping () -> Void) -> some View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:oncancellation:))*