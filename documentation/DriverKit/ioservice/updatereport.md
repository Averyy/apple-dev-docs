# UpdateReport

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn UpdateReport(OSData * channels, uint32_t action, uint32_t * outElementCount, uint64_t offset, uint64_t capacity, IOMemoryDescriptor * buffer);
```

## See Also

- [AdjustBusy](ioservice/adjustbusy.md)
- [ClientCrashed](ioservice/clientcrashed.md)
- [ConfigureReport](ioservice/configurereport.md)
- [CopyName](ioservice/copyname.md)
- [CopyProviderProperties](ioservice/copyproviderproperties.md)
- [CopySystemStateNotificationService](ioservice/copysystemstatenotificationservice.md)
- [CoreAnalyticsSendEvent](ioservice/coreanalyticssendevent.md)
- [CreateDefaultDispatchQueue](ioservice/createdefaultdispatchqueue.md)
- [GetBusyState](ioservice/getbusystate.md)
- [GetProvider](ioservice/getprovider.md)
- [JoinPMTree](ioservice/joinpmtree.md)
- [RemoveProperty](ioservice/removeproperty.md)
- [RequireMaxBusStall](ioservice/requiremaxbusstall.md)
- [SetLegend](ioservice/setlegend.md)
- [SetPowerOverride](ioservice/setpoweroverride.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/updatereport)*