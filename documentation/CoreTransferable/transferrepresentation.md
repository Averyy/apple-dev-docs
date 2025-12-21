# TransferRepresentation

**Framework**: Core Transferable  
**Kind**: protocol

A declarative description of the process of importing and exporting a transferable item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol TransferRepresentation<Item> : Sendable
```

#### Overview

Combine multiple existing transfer representations to compose a single transfer representation that describes how to transfer an item in multiple scenarios.

The following shows a `Greeting` type that transfers both as a `Codable` type and by proxy through its `message` string.

```swift
import UniformTypeIdentifiers

struct Greeting: Codable, Transferable {
    let message: String
    var displayInAllCaps: Bool = false

    static var transferRepresentation: some TransferRepresentation {
        CodableRepresentation(contentType: .greeting)
        ProxyRepresentation(exporting: \.message)
    }
}

extension UTType {
    static let greeting = UTType(exportedAs: "com.example.greeting")
}
```

## Topics

### Implementing a transfer representation
- [var body: Self.Body](transferrepresentation/body-swift.property.md)
  A builder expression that describes the process of importing and exporting an item.
- [associatedtype Body : TransferRepresentation](transferrepresentation/body-swift.associatedtype.md)
  The transfer representation for the item.
- [associatedtype Item : Transferable](transferrepresentation/item.md)
  The type of the item that’s being transferred.
### Configuring exports
- [func exportingCondition((Self.Item) -> Bool) -> _ConditionalTransferRepresentation<Self>](transferrepresentation/exportingcondition(_:).md)
  Prevents the system from exporting an item if it does not meet the supplied condition.
### Controlling visibility
- [func visibility(TransferRepresentationVisibility) -> some TransferRepresentation<Self.Item>
](transferrepresentation/visibility(_:).md)
  Specifies the kinds of apps and processes that can see an item in transit.
### Instance Methods
- [func suggestedFileName(String) -> some TransferRepresentation<Self.Item>
](transferrepresentation/suggestedfilename(_:)-2yln2.md)
  Provides a filename to use if the receiver chooses to write the item to disk.
- [func suggestedFileName((Self.Item) -> String?) -> some TransferRepresentation<Self.Item>
](transferrepresentation/suggestedfilename(_:)-47rg0.md)
  Provides a filename to use if the receiver chooses to write the item to disk.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [CodableRepresentation](codablerepresentation.md)
- [DataRepresentation](datarepresentation.md)
- [FileRepresentation](filerepresentation.md)
- [ProxyRepresentation](proxyrepresentation.md)
- [TupleTransferRepresentation](tupletransferrepresentation.md)

## See Also

- [protocol Transferable](transferable.md)
  A protocol that describes how a type interacts with transport APIs such as drag and drop or copy and paste.
- [Choosing a transfer representation for a model type](choosing-a-transfer-representation-for-a-model-type.md)
  Define a custom representation for your data using a combination of built-in types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferrepresentation)*