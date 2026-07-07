# acquire()

**Framework**: Core NFC  
**Kind**: method

Acquire a presentment intent assertion instance from the system.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
static func acquire() async throws -> NFCPresentmentIntentAssertion
```

#### Return Value

A presentment intent assertion instance you use to prevent the default contactless app from launching.

#### Discussion

The returned object remains valid until any of the following occur:

- Your app goes into the background.
- The maximum presentment intent assertion duration expires.
- The object deinitializes.

If the system can’t create a presentment intent assertion object, this method throws an error of type [`NFCPresentmentIntentAssertion.Error`](nfcpresentmentintentassertion/error.md).

> ⚠️ **Warning**:  Check to see if the device is capable of using NFC with the [`NFCReaderSession`](nfcreadersession-swift.class.md) class property [`readingAvailable`](nfcreadersession-swift.class/readingavailable.md). Attempting to acquire a presentment intent assertion on a device that can’t use NFC raises [`fatalError(_:file:line:)`](https://developer.apple.com/documentation/Swift/fatalError(_:file:line:)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcpresentmentintentassertion/acquire())*