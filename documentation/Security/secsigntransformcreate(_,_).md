# SecSignTransformCreate(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a signing transform object.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecSignTransformCreate(_ key: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

```c
SecTransformRefSecSignTransformCreate(SecKeyRef key, CFErrorRef*error);
```

## Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free this object’s memory when you are done with it.

## Discussion

This function creates a transform which computes a cryptographic signature. The [`kSecInputIsAttributeName`](./ksecinputisattributename.md) attribute defaults to [`kSecInputIsPlainText`](./ksecinputisplaintext.md), and the [`kSecDigestTypeAttribute`](./ksecdigesttypeattribute.md) and [`kSecDigestLengthAttribute`](./ksecdigestlengthattribute.md) attributes default to something appropriate for the type of key you have supplied.

## Parameters

- `key`: A [`SecKey`](./seckey.md) with the private key used for signing.
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md). This pointer will be set if an error occurred. This value may be `NULL` if you do not want an error returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secsigntransformcreate(_:_:))*