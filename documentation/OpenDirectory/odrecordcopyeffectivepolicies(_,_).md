# ODRecordCopyEffectivePolicies(_:_:)

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst
- macOS 10.9+ - Deprecated in 10.10

> **Deprecated**: use ODRecordAuthenticationAllowed and similar functions

## Declaration

```swift
func ODRecordCopyEffectivePolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!
```

```c
extern CFDictionaryRefODRecordCopyEffectivePolicies(ODRecordRef record, CFErrorRef*error);
```

## See Also

### Functions
- [func ODNodeAddAccountPolicy(ODNodeRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodeaddaccountpolicy%28_,_,_,_%29.md)
- [func ODNodeCopyAccountPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary!](./odnodecopyaccountpolicies%28_,_%29.md)
- [func ODNodeCopyPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odnodecopypolicies%28_,_%29.md)
- [func ODNodeCopySupportedPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odnodecopysupportedpolicies%28_,_%29.md)
- [func ODNodeCustomFunction(ODNodeRef!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFTypeRef!](./odnodecustomfunction%28_,_,_,_%29.md)
- [func ODNodePasswordContentCheck(ODNodeRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodepasswordcontentcheck%28_,_,_,_%29.md)
- [func ODNodeRemoveAccountPolicy(ODNodeRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnoderemoveaccountpolicy%28_,_,_,_%29.md)
- [func ODNodeRemovePolicy(ODNodeRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnoderemovepolicy%28_,_,_%29.md)
- [func ODNodeSetAccountPolicies(ODNodeRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodesetaccountpolicies%28_,_,_%29.md)
- [func ODNodeSetPolicies(ODNodeRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodesetpolicies%28_,_,_%29.md)
- [func ODNodeSetPolicy(ODNodeRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodesetpolicy%28_,_,_,_%29.md)
- [func ODRecordAddAccountPolicy(ODRecordRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordaddaccountpolicy%28_,_,_,_%29.md)
- [func ODRecordAuthenticationAllowed(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordauthenticationallowed%28_,_%29.md)
- [func ODRecordCopyAccountPolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary!](./odrecordcopyaccountpolicies%28_,_%29.md)
- [func ODRecordCopyPolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odrecordcopypolicies%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecordcopyeffectivepolicies(_:_:))*