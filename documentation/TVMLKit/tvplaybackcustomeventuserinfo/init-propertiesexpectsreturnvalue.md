# init(properties:expectsReturnValue:)

**Framework**: TVMLKit  
**Kind**: init

Create a new custom playback event user info dictionary.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
init(properties: [TVPlaybackEventProperty : Any]?, expectsReturnValue: Bool)
```

#### Return Value

A Boolean value that indicates whether the custom playback event requires a return value.

#### Discussion

When created, if the function requires a return value, it is only dispatched to first listener. Otherwise, it is broadcast to all of the listeners.

## Parameters

- `properties`: A dictionary of custom playback event properties.

## See Also

- [struct TVPlaybackEventProperty](tvplaybackeventproperty.md)
  Extend this structure to create your own custom playback event properties.
- [var expectsReturnValue: Bool](tvplaybackcustomeventuserinfo/expectsreturnvalue.md)
  A Boolean value that indicates whether the custom event expects to contain a return value.
- [var returnValue: Any?](tvplaybackcustomeventuserinfo/returnvalue.md)
  The return value type for the custom event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackcustomeventuserinfo/init(properties:expectsreturnvalue:))*