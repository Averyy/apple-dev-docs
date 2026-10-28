# setTo(_:)

**Framework**: Scripting Bridge  
**Kind**: method  
**Role**: Instance Method

Sets the receiver to a specified value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func setTo(_ value: Any?)
```

```objc
- (void) setTo:(id) value;
```

## Discussion

You should not call this method directly.

## Parameters

- `value`: The data the receiver should be set to. It can be an [`NSString`](../../Foundation/nsstring.md), [`NSNumber`](../../Foundation/nsnumber.md), [`NSArray`](../../Foundation/nsarray.md), `SBObject`, or any other type of object supported by the Scripting Bridge framework.

## See Also

### Sending Apple Events
- [- sendEvent:id:parameters:](./sendevent_id_parameters_.md)
  Sends an Apple event with the given event class, event ID, and format to the target application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/setto(_:))*