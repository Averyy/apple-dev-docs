# UpdateReport

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual IOReturn UpdateReport(OSData *channels, uint32_t action, uint32_t *outElementCount, uint64_t offset, uint64_t capacity, IOMemoryDescriptor *buffer);
```

## See Also

### Instance Methods
- [AdjustBusy](./adjustbusy.md)
- [ClientCrashed](./clientcrashed.md)
- [ConfigureReport](./configurereport.md)
- [CopyName](./copyname.md)
- [CopyProviderProperties](./copyproviderproperties.md)
- [CopySystemStateNotificationService](./copysystemstatenotificationservice.md)
- [CoreAnalyticsSendEvent](./coreanalyticssendevent.md)
- [CreateDefaultDispatchQueue](./createdefaultdispatchqueue.md)
- [GetBusyState](./getbusystate.md)
- [GetProvider](./getprovider.md)
- [JoinPMTree](./joinpmtree.md)
- [RemoveProperty](./removeproperty.md)
- [RequireMaxBusStall](./requiremaxbusstall.md)
- [SetLegend](./setlegend.md)
- [SetPowerOverride](./setpoweroverride.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/updatereport)*