# TransferRepresentation Implementations

**Framework**: Core Transferable

## Topics

### Instance Methods
- [func exportingCondition((Self.Item) -> Bool) -> _ConditionalTransferRepresentation<Self>](codablerepresentation/exportingcondition(_:).md)
  Prevents the system from exporting an item if it does not meet the supplied condition.
- [func suggestedFileName((Self.Item) -> String?) -> some TransferRepresentation<Self.Item>
](codablerepresentation/suggestedfilename(_:)-1ixmb.md)
  Provides a filename to use if the receiver chooses to write the item to disk.
- [func suggestedFileName(String) -> some TransferRepresentation<Self.Item>
](codablerepresentation/suggestedfilename(_:)-9xa3h.md)
  Provides a filename to use if the receiver chooses to write the item to disk.
- [func visibility(TransferRepresentationVisibility) -> some TransferRepresentation<Self.Item>
](codablerepresentation/visibility(_:).md)
  Specifies the kinds of apps and processes that can see an item in transit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/codablerepresentation/transferrepresentation-implementations)*