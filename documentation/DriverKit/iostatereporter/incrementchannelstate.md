# incrementChannelState

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn incrementChannelState(uint64_t channel_id, uint64_t state_id, uint64_t time_in_state, uint64_t intransitions, uint64_t last_intransition);
```

## See Also

- [getStateInTransitions](iostatereporter/getstateintransitions.md)
- [getStateLastChannelUpdateTime](iostatereporter/getstatelastchannelupdatetime.md)
- [getStateLastTransitionTime](iostatereporter/getstatelasttransitiontime.md)
- [getStateResidencyTime](iostatereporter/getstateresidencytime.md)
- [initWith](iostatereporter/initwith.md)
- [overrideChannelState](iostatereporter/overridechannelstate.md)
- [setChannelState](iostatereporter/setchannelstate-9hd9n.md)
- [setChannelState](iostatereporter/setchannelstate-7n3or.md)
- [setState](iostatereporter/setstate-96bfi.md)
- [setState](iostatereporter/setstate-1puxp.md)
- [setStateByIndices](iostatereporter/setstatebyindices-6dmm5.md)
- [setStateByIndices](iostatereporter/setstatebyindices-13fxh.md)
- [setStateID](iostatereporter/setstateid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iostatereporter/incrementchannelstate)*