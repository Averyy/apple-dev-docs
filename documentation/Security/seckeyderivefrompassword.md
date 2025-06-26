# SecKeyDeriveFromPassword(_:_:_:)

**Framework**: Security  
**Kind**: func

Returns a key object in which the key data is derived from a password.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecKeyDeriveFromPassword(_ password: CFString, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

#### Return Value

The derived key object, or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free the key’s memory when you are done with it.

#### Discussion

The parameters dictionary must contain at least the following keys:

- [`kSecKeyKeyType`](kseckeykeytype.md)—the type of symmetric key to generate.
- [`kSecAttrSalt`](ksecattrsalt.md)—a `CFDataRef` object containing the salt value that is mixed into the pseudorandom rounds.

The parameters dictionary may contain the following optional keys:

- [`kSecAttrPRF`](ksecattrprf.md) - the algorithm to use for the pseudorandom-function.

If zero, this defaults to [`kSecAttrPRFHmacAlgSHA1`](ksecattrprfhmacalgsha1.md). For a list of possible values, see `kSecAttrPRF Value Constants`.

- [`kSecAttrRounds`](ksecattrrounds.md)—the number of times to call the pseudorandom function. If zero, the count is computed so that computation will take 1/10 of a second (on average).
- [`kSecAttrKeySizeInBits`](ksecattrkeysizeinbits.md)—a `CFNumberRef` value containing the requested key size in bits. The key size must be valid for the key type. Defaults to 128 if not provided.

## Parameters

- `password`: The password from which the key should be derived.
- `parameters`: A set of parameters for deriving the password.
- `error`: A pointer to a   variable where an error object is stored upon failure. If not  , the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyderivefrompassword(_:_:_:))*