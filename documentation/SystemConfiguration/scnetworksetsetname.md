# SCNetworkSetSetName(_:_:)

**Framework**: System Configuration  
**Kind**: func

Stores the user-specified name for the specified set.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkSetSetName(_ set: SCNetworkSet, _ name: CFString?) -> Bool
```

#### Return Value

`TRUE` if the name was saved; `FALSE` if an error occurred.

#### Discussion

Although it is not technically required, the user-specified names for all sets should be unique. For this reason, an error is returned if you attempt to name two sets with the same string.

## Parameters

- `set`: The set (the complete configuration for a single location).
- `name`: The user-defined name to associate with the set.

## See Also

- [func SCNetworkSetAddService(SCNetworkSet, SCNetworkService) -> Bool](scnetworksetaddservice(_:_:).md)
  Adds the specified network service to the specified set.
- [func SCNetworkSetContainsInterface(SCNetworkSet, SCNetworkInterface) -> Bool](scnetworksetcontainsinterface(_:_:).md)
  Returns a Boolean value indicating whether the specified interface is represented by at least one network service in the specified set.
- [func SCNetworkSetCopy(SCPreferences, CFString) -> SCNetworkSet?](scnetworksetcopy(_:_:).md)
  Returns the set with the specified identifier.
- [func SCNetworkSetCopyAll(SCPreferences) -> CFArray?](scnetworksetcopyall(_:).md)
  Returns all available sets for the specified preferences session.
- [func SCNetworkSetCopyCurrent(SCPreferences) -> SCNetworkSet?](scnetworksetcopycurrent(_:).md)
  Returns the current set.
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
- [func SCNetworkSetSetServiceOrder(SCNetworkSet, CFArray) -> Bool](scnetworksetsetserviceorder(_:_:).md)
  Stores the user-specified ordering of network services for the specified set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworksetsetname(_:_:))*