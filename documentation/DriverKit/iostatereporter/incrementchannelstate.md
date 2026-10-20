# incrementChannelState

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
IOReturn incrementChannelState(uint64_t channel_id, uint64_t state_id, uint64_t time_in_state, uint64_t intransitions, uint64_t last_intransition);
```

## See Also

### Instance Methods
- [getStateInTransitions](./getstateintransitions.md)
- [getStateLastChannelUpdateTime](./getstatelastchannelupdatetime.md)
- [getStateLastTransitionTime](./getstatelasttransitiontime.md)
- [getStateResidencyTime](./getstateresidencytime.md)
- [initWith](./initwith.md)
- [overrideChannelState](./overridechannelstate.md)
- [setChannelState](./setchannelstate-9hd9n.md)
- [setChannelState](./setchannelstate-7n3or.md)
- [setState](./setstate-96bfi.md)
- [setState](./setstate-1puxp.md)
- [setStateByIndices](./setstatebyindices-6dmm5.md)
- [setStateByIndices](./setstatebyindices-13fxh.md)
- [setStateID](./setstateid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iostatereporter/incrementchannelstate)*