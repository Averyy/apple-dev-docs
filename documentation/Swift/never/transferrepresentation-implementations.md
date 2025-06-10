# TransferRepresentation Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var body: Never](never/body-swift.property.md)
  A builder expression that describes the process of importing and exporting an item.
### Instance Methods
- [func exportingCondition((Self.Item) -> Bool) -> _ConditionalTransferRepresentation<Self>](never/exportingcondition(_:).md)
  Prevents the system from exporting an item if it does not meet the supplied condition.
- [func suggestedFileName((Self.Item) -> String?) -> some TransferRepresentation<Self.Item>
](never/suggestedfilename(_:)-3oljg.md)
  Provides a filename to use if the receiver chooses to write the item to disk.
- [func suggestedFileName(String) -> some TransferRepresentation<Self.Item>
](never/suggestedfilename(_:)-940ze.md)
  Provides a filename to use if the receiver chooses to write the item to disk.
- [func visibility(TransferRepresentationVisibility) -> some TransferRepresentation<Self.Item>
](never/visibility(_:).md)
  Specifies the kinds of apps and processes that can see an item in transit.
### Type Aliases
- [typealias Body](never/body-swift.typealias.md)
  The transfer representation for the item.
- [typealias Item](never/item.md)
  The type of the item that’s being transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/transferrepresentation-implementations)*