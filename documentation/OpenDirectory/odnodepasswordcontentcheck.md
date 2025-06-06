# ODNodePasswordContentCheck(_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func

**Availability**:
- Mac Catalyst ?+
- macOS 10.10+

## Declaration

```swift
func ODNodePasswordContentCheck(_ node: ODNodeRef!, _ password: CFString!, _ recordName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

## See Also

- [func ODNodeAddAccountPolicy(ODNodeRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodeaddaccountpolicy(_:_:_:_:).md)
- [func ODNodeCopyAccountPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary!](odnodecopyaccountpolicies(_:_:).md)
- [func ODNodeCopyPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odnodecopypolicies(_:_:).md)
- [func ODNodeCopySupportedPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odnodecopysupportedpolicies(_:_:).md)
- [func ODNodeCustomFunction(ODNodeRef!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFTypeRef!](odnodecustomfunction(_:_:_:_:).md)
- [func ODNodeRemoveAccountPolicy(ODNodeRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnoderemoveaccountpolicy(_:_:_:_:).md)
- [func ODNodeRemovePolicy(ODNodeRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnoderemovepolicy(_:_:_:).md)
- [func ODNodeSetAccountPolicies(ODNodeRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodesetaccountpolicies(_:_:_:).md)
- [func ODNodeSetPolicies(ODNodeRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodesetpolicies(_:_:_:).md)
- [func ODNodeSetPolicy(ODNodeRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodesetpolicy(_:_:_:_:).md)
- [func ODRecordAddAccountPolicy(ODRecordRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordaddaccountpolicy(_:_:_:_:).md)
- [func ODRecordAuthenticationAllowed(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordauthenticationallowed(_:_:).md)
- [func ODRecordCopyAccountPolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary!](odrecordcopyaccountpolicies(_:_:).md)
- [func ODRecordCopyEffectivePolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odrecordcopyeffectivepolicies(_:_:).md)
- [func ODRecordCopyPolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odrecordcopypolicies(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnodepasswordcontentcheck(_:_:_:_:))*