# SecKeyCreateWithData(_:_:_:)

**Framework**: Security  
**Kind**: func

Restores a key from an external representation of that key.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func SecKeyCreateWithData(_ keyData: CFData, _ attributes: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

## Mentions

- [Storing Keys as Data](storing-keys-as-data.md)

#### Return Value

The restored key or `NULL` on failure. In Objective-C, call [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to free the key’s memory when you are done with it.

## Parameters

- `keyData`: Data representing the key. The format of the data depends on the type of key being created. See the description of the return value of the   function for details.
- `attributes`: A dictionary containing attributes describing the key to be imported. This dictionary must include at least the following keys:
- `error`: The address of a  doc://com.apple.documentation/documentation/corefoundation/cferror-ru8  object. If an error occurs, this is set to point at an error instance that describes the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycreatewithdata(_:_:_:))*