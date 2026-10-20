# fileExporterFilenameLabel(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

On macOS, configures the `fileExporter` with a label for the file name field.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated func fileExporterFilenameLabel(_ label: LocalizedStringResource) -> some View
```

**Other overloads**:

```swift
nonisolated
func fileExporterFilenameLabel(_ label: Text?) -> some View
```

```swift
nonisolated
func fileExporterFilenameLabel(_ labelKey: LocalizedStringKey) -> some View
```

```swift
nonisolated
func fileExporterFilenameLabel<S>(_ label: S) -> some View where S : StringProtocol
```

## Parameters

- `label`: The localized string resource to display.

## See Also

### Exporting to file
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType?, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: (() -> Void)?) -> some View](./fileexporter%28ispresented,document,contenttype,defaultfilename,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to export a `WritableDocument` to a file on disk.
- [func fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](./fileexporter%28ispresented,documents,contenttypes,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to export a collection of objects conforming to `WritableDocument` to files on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](./fileexporter%28ispresented,item,contenttypes,defaultfilename,oncompletion,oncancellation%29.md)
  Presents a system dialog allowing the user to export a `Transferable` item to a file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](./fileexporter%28ispresented,items,contenttypes,oncompletion,oncancellation%29.md)
  Presents a system dialog allowing the user to export a collection of `Transferable` items to files on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporterfilenamelabel(_:))*