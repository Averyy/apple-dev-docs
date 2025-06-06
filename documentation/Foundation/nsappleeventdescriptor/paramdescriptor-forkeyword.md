# paramDescriptor(forKeyword:)

**Framework**: Foundation  
**Kind**: method

Returns a descriptor for the receiver’s Apple event parameter identified by the specified keyword.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func paramDescriptor(forKeyword keyword: AEKeyword) -> NSAppleEventDescriptor?
```

#### Return Value

A descriptor for the specified keyword, or `nil` if an error occurs.

#### Discussion

The receiver must be an Apple event.

## Parameters

- `keyword`: A keyword (a four-character code) that identifies the parameter descriptor to obtain.

## See Also

- [func attributeDescriptor(forKeyword: AEKeyword) -> NSAppleEventDescriptor?](nsappleeventdescriptor/attributedescriptor(forkeyword:).md)
  Returns a descriptor for the receiver’s Apple event attribute identified by the specified keyword.
- [var eventClass: AEEventClass](nsappleeventdescriptor/eventclass.md)
  The event class for the receiver.
- [var eventID: AEEventID](nsappleeventdescriptor/eventid.md)
  The event ID for the receiver.
- [func removeParamDescriptor(withKeyword: AEKeyword)](nsappleeventdescriptor/removeparamdescriptor(withkeyword:).md)
  Removes the receiver’s parameter descriptor identified by the specified keyword.
- [var returnID: AEReturnID](nsappleeventdescriptor/returnid.md)
  The receiver’s return ID (the ID for a reply Apple event).
- [func setAttribute(NSAppleEventDescriptor, forKeyword: AEKeyword)](nsappleeventdescriptor/setattribute(_:forkeyword:).md)
  Adds a descriptor to the receiver as an attribute identified by the specified keyword.
- [func setParam(NSAppleEventDescriptor, forKeyword: AEKeyword)](nsappleeventdescriptor/setparam(_:forkeyword:).md)
  Adds a descriptor to the receiver as an Apple event parameter identified by the specified keyword.
- [var transactionID: AETransactionID](nsappleeventdescriptor/transactionid.md)
  The receiver’s transaction ID, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/paramdescriptor(forkeyword:))*