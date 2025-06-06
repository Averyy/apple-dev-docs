# TransferRepresentation Implementations

**Framework**: Core Transferable

## Topics

### Instance Methods
- [func exportingCondition((Self.Item) -> Bool) -> _ConditionalTransferRepresentation<Self>](datarepresentation/exportingcondition(_:).md)
  Prevents the system from exporting an item if it does not meet the supplied condition.
- [func suggestedFileName(String) -> some TransferRepresentation<Self.Item>
](datarepresentation/suggestedfilename(_:)-3p1cr.md)
  Provides a filename to use if the receiver chooses to write the item to disk.
- [func suggestedFileName((Self.Item) -> String?) -> some TransferRepresentation<Self.Item>
](datarepresentation/suggestedfilename(_:)-6zayd.md)
  Provides a filename to use if the receiver chooses to write the item to disk.
- [func visibility(TransferRepresentationVisibility) -> some TransferRepresentation<Self.Item>
](datarepresentation/visibility(_:).md)
  Specifies the kinds of apps and processes that can see an item in transit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/datarepresentation/transferrepresentation-implementations)*