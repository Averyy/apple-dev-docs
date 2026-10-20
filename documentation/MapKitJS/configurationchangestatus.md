# ConfigurationChangeStatus

**Framework**: MapKit JS  
**Kind**: enum  
**Role**: Enumeration

Values that represent the status of a configuration change.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
const ConfigurationChangeStatus: Readonly<{
    readonly Initialized: "Initialized";
    readonly Refreshed: "Refreshed";
}>
type ConfigurationChangeStatus =
    (typeof ConfigurationChangeStatus)[keyof typeof ConfigurationChangeStatus];
```

## Topics

### Enumeration Cases
- [Initialized](./configurationchangestatus/initialized.md)
  A status value that indicates the initialization of the configuration is successful.
- [Refreshed](./configurationchangestatus/refreshed.md)
  A status value that indicates the configuration refresh is successful.

## See Also

### Initialization and error status
- [const ConfigurationErrorStatus](./configurationerrorstatus.md)
  A value that represents the status of a configuration error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/configurationchangestatus)*