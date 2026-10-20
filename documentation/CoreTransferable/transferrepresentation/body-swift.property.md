# body

**Framework**: Core Transferable  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A builder expression that describes the process of importing and exporting an item.

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
@TransferRepresentationBuilder
<Self.Item> var body: Self.Body { get }
```

#### Discussion

Combine multiple existing transfer representations to compose a single transfer representation that describes how to transfer an item in multiple scenarios.

```swift
struct CombinedRepresentation: TransferRepresentation {
   var body: some TransferRepresentation {
       DataRepresentation(...)
       FileRepresentation(...)
   }
}
```

## See Also

### Implementing a transfer representation
- [associatedtype Body : TransferRepresentation](./body-swift.associatedtype.md)
  The transfer representation for the item.
- [associatedtype Item : Transferable](./item.md)
  The type of the item that’s being transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferrepresentation/body-swift.property)*