# setAttribute(_:forKeyword:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a descriptor to the receiver as an attribute identified by the specified keyword.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setAttribute(_ descriptor: NSAppleEventDescriptor, forKeyword keyword: AEKeyword)
```

```objc
- (void) setAttributeDescriptor:(NSAppleEventDescriptor *) descriptor forKeyword:(AEKeyword) keyword;
```

## Discussion

The receiver must be an Apple event. Currently provides no indication if an error occurs.

## Parameters

- `descriptor`: The attribute descriptor to add to the receiver.
- `keyword`: A keyword (a four-character code) that identifies the attribute descriptor to add. If a descriptor with that keyword already exists in the receiver, it is replaced.

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
- [func setParam(NSAppleEventDescriptor, forKeyword: AEKeyword)](./setparam%28_,forkeyword%29.md)
  Adds a descriptor to the receiver as an Apple event parameter identified by the specified keyword.
- [var transactionID: AETransactionID](./transactionid.md)
  The receiver’s transaction ID, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/setattribute(_:forkeyword:))*