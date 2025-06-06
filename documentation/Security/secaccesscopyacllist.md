# SecAccessCopyACLList(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves all the ACL entries of a given access instance.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecAccessCopyACLList(_ accessRef: SecAccess, _ aclList: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

An access instance can have any number of ACL entries for specific operations or sets of operations. Use this method to get an array of all the ACL entries of a particular access instance. To retrieve entries corresponding to specific operations, use the [`SecAccessCopyMatchingACLList(_:_:)`](secaccesscopymatchingacllist(_:_:).md) method instead.

## Parameters

- `accessRef`: The access instance from which to retrieve the information.
- `aclList`: A pointer the method uses to return an array of   instances. In Objective-C, call the   function to release the array when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscopyacllist(_:_:))*