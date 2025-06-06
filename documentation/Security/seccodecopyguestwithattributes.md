# SecCodeCopyGuestWithAttributes(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Asks a code host to identify one of its guests given the type and value of specific attributes of the guest code.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SecCodeCopyGuestWithAttributes(_ host: SecCode?, _ attributes: CFDictionary?, _ flags: SecCSFlags, _ guest: UnsafeMutablePointer<SecCode?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md). In particular:

#### Discussion

Different hosts support different types and combinations of attributes. The methods a host uses to identify, separate, and control its guests are specific to each type of host. This function provides a generic abstraction layer that allows uniform interrogation of all hosts.

The most frequent use of this function is to obtain a code object for specific code. To do that, pass `NULL` for the `host` parameter and specify all the attributes you have for the guest. You can also use this function to crawl through the guest hosting structure in incremental steps. To do so, pass in a specific host and the attributes for a particular guest.

## Parameters

- `host`: A valid code object representing code running on the system that acts as a host for signed code. Pass   to indicate that the code signing root of trust (currently, the system kernel) should be used as the code host.
- `attributes`: A dictionary containing zero or more attribute values to be used in identifying guest code. See   for possible dictionary keys and descriptions of the associated values. Each host supports only particular combinations of keys and values, and the function returns an error if any unsupported set is requested. Pass   to indicate an empty attribute set. Note that some hosts that support hosting chains (guests being hosts) may return sub-guests to this function; that is, the code object returned by this call may not be a direct guest of the queried host, although it will be a guest somewhere in the hosting chain.
- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.
- `guest`: On return, a code object identifying the particular guest of the host that has the specified attribute values. If the attributes specify the host itself, the function returns the code object for the host. If more than one guest meet the specified criteria, the function returns the result  .

## See Also

- [func SecCodeCopyHost(SecCode, SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](seccodecopyhost(_:_:_:).md)
  Retrieves the code object for the host of specified guest code.
- [func SecCodeCopyStaticCode(SecCode, SecCSFlags, UnsafeMutablePointer<SecStaticCode?>) -> OSStatus](seccodecopystaticcode(_:_:_:).md)
  Returns a static code object representing the on-disk version of the given running code.
- [func SecCodeCopySelf(SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](seccodecopyself(_:_:).md)
  Retrieves the code object for the code making the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecopyguestwithattributes(_:_:_:_:))*