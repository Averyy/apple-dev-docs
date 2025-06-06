# SCNetworkSetCopyCurrent(_:)

**Framework**: System Configuration  
**Kind**: func

Returns the current set.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkSetCopyCurrent(_ prefs: SCPreferences) -> SCNetworkSet?
```

#### Return Value

The current set, or `NULL` if no current set has been defined.

## Parameters

- `prefs`: The preferences session.

## See Also

- [func SCNetworkSetAddService(SCNetworkSet, SCNetworkService) -> Bool](scnetworksetaddservice(_:_:).md)
  Adds the specified network service to the specified set.
- [func SCNetworkSetContainsInterface(SCNetworkSet, SCNetworkInterface) -> Bool](scnetworksetcontainsinterface(_:_:).md)
  Returns a Boolean value indicating whether the specified interface is represented by at least one network service in the specified set.
- [func SCNetworkSetCopy(SCPreferences, CFString) -> SCNetworkSet?](scnetworksetcopy(_:_:).md)
  Returns the set with the specified identifier.
- [func SCNetworkSetCopyAll(SCPreferences) -> CFArray?](scnetworksetcopyall(_:).md)
  Returns all available sets for the specified preferences session.
- [func SCNetworkSetCopyServices(SCNetworkSet) -> CFArray?](scnetworksetcopyservices(_:).md)
  Returns all network services associated with the specified set.
- [func SCNetworkSetCreate(SCPreferences) -> SCNetworkSet?](scnetworksetcreate(_:).md)
  Creates a new set in the configuration.
- [func SCNetworkSetGetName(SCNetworkSet) -> CFString?](scnetworksetgetname(_:).md)
  Returns the user-specified name associated with the specified set.
- [func SCNetworkSetGetServiceOrder(SCNetworkSet) -> CFArray?](scnetworksetgetserviceorder(_:).md)
  Returns the user-specified ordering of network services within the specified set.
- [func SCNetworkSetGetSetID(SCNetworkSet) -> CFString?](scnetworksetgetsetid(_:).md)
  Returns the identifier for the specified set.
- [func SCNetworkSetGetTypeID() -> CFTypeID](scnetworksetgettypeid().md)
  Returns the type identifier of all `SCNetworkSet` instances.
- [func SCNetworkSetRemove(SCNetworkSet) -> Bool](scnetworksetremove(_:).md)
  Removes the specified set from the configuration.
- [func SCNetworkSetRemoveService(SCNetworkSet, SCNetworkService) -> Bool](scnetworksetremoveservice(_:_:).md)
  Removes the specified network service from the specified set.
- [func SCNetworkSetSetCurrent(SCNetworkSet) -> Bool](scnetworksetsetcurrent(_:).md)
  Specifies the set that should be the current set.
- [func SCNetworkSetSetName(SCNetworkSet, CFString?) -> Bool](scnetworksetsetname(_:_:).md)
  Stores the user-specified name for the specified set.
- [func SCNetworkSetSetServiceOrder(SCNetworkSet, CFArray) -> Bool](scnetworksetsetserviceorder(_:_:).md)
  Stores the user-specified ordering of network services for the specified set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworksetcopycurrent(_:))*