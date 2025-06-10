# Choosing a transfer representation for a model type

**Framework**: Core Transferable

Define a custom representation for your data using a combination of built-in types.

#### Overview

When you enable types in your app to participate in system interactions like sharing or drag and drop, you get to decide how — and if — you expose your app’s model data to other apps. You can also control how different parts of your own app respond to receiving your models in different contexts.

Core Transferable defines a set of transfer representations and modifiers that you can combine together in different ways to get the behavior that’s right for the different data transfer and sharing scenarios your app supports. For each of your app’s model types that participate in sharing and data transfer, pick the built-in transfer representations to represent your model’s data, or define your own. Then, determine whether your app allows people to share or receive the model’s data, or both.

##### Compose Transfer Representations

Core Transferable defines three main transfer representations: [`DataRepresentation`](datarepresentation.md), [`FileRepresentation`](filerepresentation.md), and [`CodableRepresentation`](codablerepresentation.md). Use [`DataRepresentation`](datarepresentation.md) for model types where the entire model is stored in memory, and use [`FileRepresentation`](filerepresentation.md) for types stored on disk.

You use [`CodableRepresentation`](codablerepresentation.md) as convenient way to create a transfer representation if your model is already `Codable` or you can easily make it `Codable`. For more information on making a type `Codable`, see [`Encoding and Decoding Custom Types`](https://developer.apple.com/documentation/Foundation/encoding-and-decoding-custom-types).

> ❗ **Important**: If you use a `CodableRepresentation`, you’re often defining a new data type as well. As a result, include corresponding entries in the app’s `Info.plist`. For more information, see [`Defining file and data types for your app`](https://developer.apple.com/documentation/UniformTypeIdentifiers/defining-file-and-data-types-for-your-app).

Use the [`ProxyRepresentation`](proxyrepresentation.md) type to let another type that conforms to `Transferable` take on the responsibility of representing your type. Common types like strings, data, and images are already `Transferable`, and you can use them as proxy representations in some common contexts.

You can combine multiple transfer representations together to support different clients or scenarios. For example, you can combine a [`CodableRepresentation`](codablerepresentation.md) with a [`ProxyRepresentation`](proxyrepresentation.md) to let your app transfer its `Note` type to different parts of the app, but still maintain compatibility with other text editors:

```swift
struct Note: Transferable {
    var title: String
    static var transferRepresentation: some TransferRepresentation {
        CodableRepresentation(contentType: .note)
        ProxyRepresentation(\.title)
    }
}

extension UTType {
     static var note: UTType { UTType(exportedAs: "com.example.note") }
}
```

The order of the transfer representations in the [`transferRepresentation`](transferable/transferrepresentation.md) builder matters: the most preferable representation comes first, followed by the less preferable — but more compatible — representations.

##### Configure Your Model Type for Import or Export

You can limit a transfer representation to support only importing, only exporting, or the representation can support both. Imports occur when your app is the recipient of an item from sharing, the  of a drag-and-drop interaction, or the  from a copy-and-paste interaction. Conversely, exports occur when people share, copy, or drag an item out of your app. For example, your vector image editing app might support exporting, but choose not to import PNG images.

Transfer representation initializers control whether representations support sharing interactions for import and export. The following shows a data representation of tax information that can only import tax forms and can only output tax returns.

```swift
struct TaxInfo {
    var forms: [TaxForm]
    var year: Int

    init(_ formsData: Data) { <# ... #> }
    func generateReturnsData() -> Data { <# ... #> }
}

extension TaxInfo: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        DataRepresentation(importedContentType: .taxForm) { formsData in
            TaxInfo(formsData)
        }
        DataRepresentation(exportedContentType: .taxReturn) { taxInfo in
            taxInfo.generateReturnsData()
        }
    }
}

extension UTType {
    static var taxForm = UTType(exportedAs: "com.example.taxForm")
    static var taxReturn = UTType(exportedAs: "com.example.taxReturn")
}
```

## See Also

- [protocol Transferable](transferable.md)
  A protocol that describes how a type interacts with transport APIs such as drag and drop or copy and paste.
- [protocol TransferRepresentation](transferrepresentation.md)
  A declarative description of the process of importing and exporting a transferable item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/choosing-a-transfer-representation-for-a-model-type)*