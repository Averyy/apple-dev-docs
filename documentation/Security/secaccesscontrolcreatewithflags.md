# SecAccessControlCreateWithFlags(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a new access control object with the specified protection type and flags.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecAccessControlCreateWithFlags(_ allocator: CFAllocator?, _ protection: CFTypeRef, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccessControl?
```

## Mentions

- [Protecting keys with the Secure Enclave](protecting-keys-with-the-secure-enclave.md)
- [Restricting keychain item accessibility](restricting-keychain-item-accessibility.md)

#### Return Value

The newly created access control object. In Objective-C, free this item with [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) when you are done with it.

#### Discussion

You use the result of this function as a value for the [`kSecAttrAccessControl`](ksecattraccesscontrol.md) attribute in the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md), [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md), or [`SecKeyGeneratePair(_:_:_:)`](seckeygeneratepair(_:_:_:).md) functions.

Accessing keychain items or performing operations on keys that are protected by access control objects may block execution on the main thread. Perform these actions in the background, or use them in combination with the [`kSecUseAuthenticationContext`](ksecuseauthenticationcontext.md) and [`kSecUseAuthenticationUI`](ksecuseauthenticationui.md) attributes to manage user interactions.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new   object. Pass   or   to allocate memory for the new allocator using the default allocator.
- `protection`: Protection class to be used for the item. Use one of the values that go with the   attribute key, namely those listed in  .
- `flags`: Flags specifying the allowed operations for the item. See  .
- `error`: On return, if an error occurred, the reference pointed at by this parameter refers to an error object that indicates the reason for failure. The caller is responsible for releasing the error object. Pass   for this parameter to ignore the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscontrolcreatewithflags(_:_:_:_:))*