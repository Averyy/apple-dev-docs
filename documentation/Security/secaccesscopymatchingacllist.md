# SecAccessCopyMatchingACLList(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves selected ACL entries from a given access instance.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecAccessCopyMatchingACLList(_ accessRef: SecAccess, _ authorizationTag: CFTypeRef) -> CFArray?
```

#### Return Value

An array containing the selected access control list entries. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) method to release the array when you are finished using it.

#### Discussion

An access instance can have any number of ACL entries for specific operations or sets of operations. This method returns the ACL entries that apply to the given operation. To retrieve all the ACL entries for an access instance, use the [`SecAccessCopyACLList(_:_:)`](secaccesscopyacllist(_:_:).md) method instead.

## Parameters

- `accessRef`: The access instance from which to retrieve the information.
- `authorizationTag`: An access control list authorization tag. See   for a list of possible values. The method returns only those ACL entries that apply to the operation indicated by this tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscopymatchingacllist(_:_:))*