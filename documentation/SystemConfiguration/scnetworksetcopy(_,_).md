# SCNetworkSetCopy(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the set with the specified identifier.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkSetCopy(_ prefs: SCPreferences, _ setID: CFString) -> SCNetworkSet?
```

```c
SCNetworkSetRefSCNetworkSetCopy(SCPreferencesRef prefs, CFStringRef setID);
```

## Return Value

The network set from the associated preferences, or `NULL` if the identifier does not exist in the preferences or if an error occurred. You must release the returned value.

## Parameters

- `prefs`: The preferences session.
- `setID`: The unique identifier for the set.

## See Also

### Configuring Network Sets
- [func SCNetworkSetAddService(SCNetworkSet, SCNetworkService) -> Bool](./scnetworksetaddservice%28_,_%29.md)
  Adds the specified network service to the specified set.
- [func SCNetworkSetContainsInterface(SCNetworkSet, SCNetworkInterface) -> Bool](./scnetworksetcontainsinterface%28_,_%29.md)
  Returns a Boolean value indicating whether the specified interface is represented by at least one network service in the specified set.
- [func SCNetworkSetCopyAll(SCPreferences) -> CFArray?](./scnetworksetcopyall%28_%29.md)
  Returns all available sets for the specified preferences session.
- [func SCNetworkSetCopyCurrent(SCPreferences) -> SCNetworkSet?](./scnetworksetcopycurrent%28_%29.md)
  Returns the current set.
- [func SCNetworkSetCopyServices(SCNetworkSet) -> CFArray?](./scnetworksetcopyservices%28_%29.md)
  Returns all network services associated with the specified set.
- [func SCNetworkSetCreate(SCPreferences) -> SCNetworkSet?](./scnetworksetcreate%28_%29.md)
  Creates a new set in the configuration.
- [func SCNetworkSetGetName(SCNetworkSet) -> CFString?](./scnetworksetgetname%28_%29.md)
  Returns the user-specified name associated with the specified set.
- [func SCNetworkSetGetServiceOrder(SCNetworkSet) -> CFArray?](./scnetworksetgetserviceorder%28_%29.md)
  Returns the user-specified ordering of network services within the specified set.
- [func SCNetworkSetGetSetID(SCNetworkSet) -> CFString?](./scnetworksetgetsetid%28_%29.md)
  Returns the identifier for the specified set.
- [func SCNetworkSetGetTypeID() -> CFTypeID](./scnetworksetgettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkSet` instances.
- [func SCNetworkSetRemove(SCNetworkSet) -> Bool](./scnetworksetremove%28_%29.md)
  Removes the specified set from the configuration.
- [func SCNetworkSetRemoveService(SCNetworkSet, SCNetworkService) -> Bool](./scnetworksetremoveservice%28_,_%29.md)
  Removes the specified network service from the specified set.
- [func SCNetworkSetSetCurrent(SCNetworkSet) -> Bool](./scnetworksetsetcurrent%28_%29.md)
  Specifies the set that should be the current set.
- [func SCNetworkSetSetName(SCNetworkSet, CFString?) -> Bool](./scnetworksetsetname%28_,_%29.md)
  Stores the user-specified name for the specified set.
- [func SCNetworkSetSetServiceOrder(SCNetworkSet, CFArray) -> Bool](./scnetworksetsetserviceorder%28_,_%29.md)
  Stores the user-specified ordering of network services for the specified set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworksetcopy(_:_:))*