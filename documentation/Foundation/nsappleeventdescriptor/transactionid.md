# transactionID

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s transaction ID, if any.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var transactionID: AETransactionID { get }
```

```objc
@property (readonly) AETransactionID transactionID;
```

## Discussion

The receiver’s transaction ID (an integer value), or 0 if an error occurs.

The receiver must be an Apple event. Currently provides no indication if an error occurs. For more information on transactions, see the description for [`appleEvent(withEventClass:eventID:targetDescriptor:returnID:transactionID:)`](./appleevent%28witheventclass,eventid,targetdescriptor,returnid,transactionid%29.md).

## See Also

### Working With Apple Event Descriptors
- [func attributeDescriptor(forKeyword: AEKeyword) -> NSAppleEventDescriptor?](./attributedescriptor%28forkeyword%29.md)
  Returns a descriptor for the receiver’s Apple event attribute identified by the specified keyword.
- [var eventClass: AEEventClass](./eventclass.md)
  The event class for the receiver.
- [var eventID: AEEventID](./eventid.md)
  The event ID for the receiver.
- [func paramDescriptor(forKeyword: AEKeyword) -> NSAppleEventDescriptor?](./paramdescriptor%28forkeyword%29.md)
  Returns a descriptor for the receiver’s Apple event parameter identified by the specified keyword.
- [func removeParamDescriptor(withKeyword: AEKeyword)](./removeparamdescriptor%28withkeyword%29.md)
  Removes the receiver’s parameter descriptor identified by the specified keyword.
- [var returnID: AEReturnID](./returnid.md)
  The receiver’s return ID (the ID for a reply Apple event).
- [func setAttribute(NSAppleEventDescriptor, forKeyword: AEKeyword)](./setattribute%28_,forkeyword%29.md)
  Adds a descriptor to the receiver as an attribute identified by the specified keyword.
- [func setParam(NSAppleEventDescriptor, forKeyword: AEKeyword)](./setparam%28_,forkeyword%29.md)
  Adds a descriptor to the receiver as an Apple event parameter identified by the specified keyword.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/transactionid)*