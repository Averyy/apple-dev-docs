# attributeDescriptor(forKeyword:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a descriptor for the receiver’s Apple event attribute identified by the specified keyword.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func attributeDescriptor(forKeyword keyword: AEKeyword) -> NSAppleEventDescriptor?
```

```objc
- (NSAppleEventDescriptor *) attributeDescriptorForKeyword:(AEKeyword) keyword;
```

#### Return Value

The attribute descriptor for the specified keyword, or `nil` if an error occurs.

#### Discussion

The receiver must be an Apple event.

## Parameters

- `keyword`: A keyword (a four-character code) that identifies the descriptor to obtain.

## See Also

### Working With Apple Event Descriptors
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
- [var transactionID: AETransactionID](./transactionid.md)
  The receiver’s transaction ID, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/attributedescriptor(forkeyword:))*