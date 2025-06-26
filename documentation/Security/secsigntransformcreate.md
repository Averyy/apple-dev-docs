# SecSignTransformCreate(_:_:)

**Framework**: Security  
**Kind**: func

Creates a signing transform object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecSignTransformCreate(_ key: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

#### Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this object’s memory when you are done with it.

#### Discussion

This function creates a transform which computes a cryptographic signature. The [`kSecInputIsAttributeName`](ksecinputisattributename.md) attribute defaults to [`kSecInputIsPlainText`](ksecinputisplaintext.md), and the [`kSecDigestTypeAttribute`](ksecdigesttypeattribute.md) and [`kSecDigestLengthAttribute`](ksecdigestlengthattribute.md) attributes default to something appropriate for the type of key you have supplied.

## Parameters

- `key`: A   with the private key used for signing.
- `error`: A pointer to a  . This pointer will be set if an error occurred. This value may be   if you do not want an error returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secsigntransformcreate(_:_:))*