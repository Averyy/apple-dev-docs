# AttributedTextFormatting.Transferable

**Framework**: SwiftUI  
**Kind**: struct

A transferable representation of an attributed string interpreted in a SwiftUI environment.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct Transferable
```

#### Overview

Use this type e.g. with drag and drop APIs or to create a [`fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)`](view/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:).md).

```swift
struct RichTextEditorView: View {
    @State private var text: AttributedString = ""
    @Environment(\.self) private var environment
    @State var fileExporterIsPresented: Bool = false

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

- [`rtfd`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct/rtfd)
- [`rtf`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct/rtf)

## Topics

### Initializers
- [init(text: AttributedString, in: EnvironmentValues)](attributedtextformatting/transferable/init(text:in:).md)
  Create a transferable representation of an attributed string as interpreted in a SwiftUI environment.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transferable](../CoreTransferable/Transferable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/transferable)*