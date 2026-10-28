# CGEventMaskBit

**Framework**: Core Graphics  
**Kind**: macro  
**Role**: Macro

Generates an event mask for a single type of event.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```c
#define CGEventMaskBit(eventType)
```

## Return Value

An event mask that represents the specified event.

## Discussion

This macro converts an event type constant into a mask. You can use this mask to specify that an event tap should observe the event. For more information, see [`CGEventMask`](./cgeventmask.md).

## Parameters

- `eventType`: An event type constant. Pass one of the constants listed in [`CGEventType`](./cgeventtype.md).

## See Also

### Working With Event Taps
- [class func tapCreate(tap: CGEventTapLocation, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](./cgevent/tapcreate%28tap,place,options,eventsofinterest,callback,userinfo%29.md)
  Creates an event tap.
- [class func tapCreateForPSN(processSerialNumber: UnsafeMutableRawPointer, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](./cgevent/tapcreateforpsn%28processserialnumber,place,options,eventsofinterest,callback,userinfo%29.md)
  Creates an event tap for a specified process.
- [class func tapEnable(tap: CFMachPort, enable: Bool)](./cgevent/tapenable%28tap,enable%29.md)
  Enables or disables an event tap.
- [class func tapIsEnabled(tap: CFMachPort) -> Bool](./cgevent/tapisenabled%28tap%29.md)
  Returns a Boolean value indicating whether an event tap is enabled.
- [func tapPostEvent(CGEventTapProxy?)](./cgevent/tappostevent%28_%29.md)
  Posts a Quartz event from an event tap into the event stream.
- [func post(tap: CGEventTapLocation)](./cgevent/post%28tap%29.md)
  Posts a Quartz event into the event stream at a specified location.
- [func postToPSN(processSerialNumber: UnsafeMutableRawPointer?)](./cgevent/posttopsn%28processserialnumber%29.md)
  Posts a Quartz event into the event stream for a specific application.
- [func CGGetEventTapList(UInt32, UnsafeMutablePointer<CGEventTapInformation>?, UnsafeMutablePointer<UInt32>?) -> CGError](./cggeteventtaplist%28_,_,_%29.md)
  Gets a list of currently installed event taps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventmaskbit)*