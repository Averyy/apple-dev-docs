# SecKeyGenerateSymmetric(_:_:)

**Framework**: Security  
**Kind**: func

Generates a random symmetric key.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecKeyGenerateSymmetric(_ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

#### Return Value

A newly generated symmetric key, or `NULL` on failure. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free the key’s memory when you are done with it.

## Parameters

- `parameters`: When used as a replacement for  , set the   key to the keychain ( ) into which the key should be stored,   to a user-visible label for the key, and   to an identifier defined by your application, for subsequent use in calls to  . Additionally, you can specify keychain access controls for the key by setting   to a   object.
- `error`: A pointer to a   variable where an error object is stored upon failure. If not  , the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeygeneratesymmetric(_:_:))*