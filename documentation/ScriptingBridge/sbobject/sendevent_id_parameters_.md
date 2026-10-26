# sendEvent:id:parameters:

**Framework**: Scripting Bridge  
**Kind**: method  
**Role**: Instance Method

Sends an Apple event with the given event class, event ID, and format to the target application.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```objc
- (id) sendEvent:(AEEventClass) eventClass id:(AEEventID) eventID parameters:(DescType) firstParamCode;
```

#### Return Value

The target application’s Apple event sent in reply; it is converted to a Cocoa object of an appropriate type.

#### Discussion

Scripting Bridge uses this method to communicate with target applications. If the target application responds to this method by sending an Apple event representing an error, the receiver calls its delegate’s [`eventDidFail(_:withError:)`](../sbapplicationdelegate/eventdidfail%28_,witherror%29.md) method. If no delegate has been assigned, the receiver raises an exception.

You should rarely have to call this method directly.

## Parameters

- `eventClass`: The event class of the Apple event to be sent.
- `eventID`: The event ID of the Apple event to be sent.

## See Also

### Sending Apple Events
- [func setTo(Any?)](./setto%28_%29.md)
  Sets the receiver to a specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/sendevent:id:parameters:)*