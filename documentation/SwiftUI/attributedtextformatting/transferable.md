# AttributedTextFormatting.Transferable

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A transferable representation of an attributed string interpreted in a SwiftUI environment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Transferable
```

## Overview

Use this type e.g. with drag and drop APIs or to create a [`fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)`](../view/fileexporter%28ispresented,item,contenttypes,defaultfilename,oncompletion,oncancellation%29.md).

```swift
struct RichTextEditorView: View {
    @State private var text: AttributedString = ""
    @Environment(\.self) private var environment
    @State private var fileExporterIsPresented: Bool = false

    var body: some View {
        TextEditor(text: $text)
            .toolbar {
                Button("Save") {
                    fileExporterIsPresented = true
                }
            }
            .fileExporter(
                isPresented: $fileExporterIsPresented,
                item: AttributedTextFormatting.Transferable(text: text, in: environment)
            ) { result in
                handleResult(result)
            }
            .dropDestination(
                for: AttributedTextFormatting.Transferable.self
            ) { transferables, _ in
                text.replaceSelection(
                    &selection,
                    with: transferables.map {
                        AttributedString(transferable: $0, in: environment)
                    }.joined(separator: AttributedString("\n")))
                return true
            }
    }
}
```

To extract text the text after importing, use attributed string’s `Foundation/AttributedString/init(transferable:in:)`.

Supported content types include:

- [`rtfd`](../../UniformTypeIdentifiers/uttype-swift.struct/rtfd.md)
- [`rtf`](../../UniformTypeIdentifiers/uttype-swift.struct/rtf.md)

## Topics

### Initializers
- [init(text: AttributedString, in: EnvironmentValues)](./transferable/init%28text,in%29.md)
  Create a transferable representation of an attributed string as interpreted in a SwiftUI environment.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Transferable](../../CoreTransferable/transferable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/transferable)*