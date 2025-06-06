# Core Transferable

**Framework**: Core Transferable  
**Kind**: module

Declare a transfer representation for your model types to participate in system sharing and data transfer operations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

#### Overview

Core Transferable provides a modern, Swift-focused approach to make your types available in data transfer and sharing contexts. Use transferable types for system interactions that move or share data, like the Share button, drag and drop, and copy and paste.

Core Transferable defines a core protocol, [`Transferable`](transferable.md), that you adopt in your app’s model types. Provide a transfer representation by composing one or more of the framework’s built-in [`TransferRepresentation`](transferrepresentation.md) types. Use `Transferable` types together with system frameworks like SwiftUI — that include types such as [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) and [`PasteButton`](https://developer.apple.com/documentation/SwiftUI/PasteButton) — to share and paste transferable data. SwiftUI also includes view modifiers like [`draggable(_:)`](https://developer.apple.com/documentation/SwiftUI/View/draggable(_:)) and [`dropDestination(for:action:isTargeted:)`](https://developer.apple.com/documentation/SwiftUI/View/dropDestination(for:action:isTargeted:)) that support drag-and-drop interactions using `Transferable`. System types like [`String`](https://developer.apple.com/documentation/Swift/String), [`Data`](https://developer.apple.com/documentation/Foundation/Data), [`URL`](https://developer.apple.com/documentation/Foundation/URL), and [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) already conform to `Transferable`.

You can send or receive `Transferable` items within an app, among a collection of your own apps, or between your apps and other apps that share an understanding of how to import or export a known data format. The following shows an example model type, `Note`, that’s extended to conform to `Transferable`:

```swift
struct Note: Codable {
    var text: String
    var url: URL

    init(url: URL) {
        self.url = url
        self.text = ""
    }
}

extension Note: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        CodableRepresentation(contentType: .note)
        ProxyRepresentation(exporting: \.text)
        FileRepresentation(
            contentType: .utf8PlainText,
            exporting: { note in SentTransferredFile(note.url) },
            importing: { received in
                let destination = URL(fileURLWithPath: <# ... #>)
                try FileManager.default.copyItem(at: received.file, to: destination)
                return Self.init(url: destination) })
        }
}

extension UTType {
    static var note = UTType(exportedAs: "com.example.note")
}
```

Use Core Transferable along with the collection of common file and data transfer identifiers from the [`Uniform Type Identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers) framework to take advantage of system interactions that move and share data using standard file types or your own custom-defined file types.

## Topics

### Essentials
- [protocol Transferable](transferable.md)
  A protocol that describes how a type interacts with transport APIs such as drag and drop or copy and paste.
- [protocol TransferRepresentation](transferrepresentation.md)
  A declarative description of the process of importing and exporting a transferable item.
- [Choosing a transfer representation for a model type](choosing-a-transfer-representation-for-a-model-type.md)
  Define a custom representation for your data using a combination of built-in types.
### Data transfer
- [struct CodableRepresentation](codablerepresentation.md)
  A transfer representation for types that participate in Swift’s protocols for encoding and decoding.
- [struct DataRepresentation](datarepresentation.md)
  A transfer representation for types that provide their own binary data conversion.
### File transfer
- [struct FileRepresentation](filerepresentation.md)
  A transfer representation for types that transfer as a file URL.
- [struct SentTransferredFile](senttransferredfile.md)
  A description of a file from the perspective of the sender.
- [struct ReceivedTransferredFile](receivedtransferredfile.md)
  A description of a file from the perspective of the receiver.
### Transfer customization
- [struct ProxyRepresentation](proxyrepresentation.md)
  A transfer representation that uses another type’s transfer representation as its own.
- [struct TransferRepresentationVisibility](transferrepresentationvisibility.md)
  The visibility levels that specify the kinds of apps and processes that can see an item in transit.
### Supporting types
- [struct TransferRepresentationBuilder](transferrepresentationbuilder.md)
  Creates a transfer representation by composing existing transfer representations.
- [struct TupleTransferRepresentation](tupletransferrepresentation.md)
  A wrapper type for tuples that contain transfer representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreTransferable)*