# fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

**Framework**: FinanceKitUI  
**Kind**: method

Presents a system dialog for allowing the user to export a collection of documents that conform to `ReferenceFileDocument` to files on disk.

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

#### Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCancellation` will be called.

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `documents`: The in-memory documents to export.
- `contentTypes`: The list of supported content types which can   be exported. If not provided,    are used.
- `onCompletion`: A callback that will be invoked when the operation has   succeeded or failed. The   indicates whether   the operation succeeded or failed.
- `onCancellation`: A callback that will be invoked   if the user cancels the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-535f4)*