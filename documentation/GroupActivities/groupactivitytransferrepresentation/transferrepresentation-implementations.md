# TransferRepresentation Implementations

**Framework**: Group Activities

## Topics

### Instance Methods
- [func exportingCondition((Self.Item) -> Bool) -> _ConditionalTransferRepresentation<Self>](groupactivitytransferrepresentation/exportingcondition(_:).md)
  Prevents the system from exporting an item if it does not meet the supplied condition.
- [func suggestedFileName((Self.Item) -> String?) -> some TransferRepresentation<Self.Item>
](groupactivitytransferrepresentation/suggestedfilename(_:)-1290n.md)
  Provides a filename to use if the receiver chooses to write the item to disk.
- [func suggestedFileName(String) -> some TransferRepresentation<Self.Item>
](groupactivitytransferrepresentation/suggestedfilename(_:)-7r3h.md)
  Provides a filename to use if the receiver chooses to write the item to disk.
- [func visibility(TransferRepresentationVisibility) -> some TransferRepresentation<Self.Item>
](groupactivitytransferrepresentation/visibility(_:).md)
  Specifies the kinds of apps and processes that can see an item in transit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitytransferrepresentation/transferrepresentation-implementations)*