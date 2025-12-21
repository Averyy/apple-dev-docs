# SecTrustCopyResult(_:)

**Framework**: Security  
**Kind**: func

Returns a dictionary containing information about an evaluated trust.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecTrustCopyResult(_ trust: SecTrust) -> CFDictionary?
```

#### Return Value

A dictionary containing keys with values that describe the result of the trust evaluation, or `NULL` when no information is available or if the trust has not been evaluated. See [`Trust Result Dictionary Keys`](trust-result-dictionary-keys.md) for the list of possible keys. In Objective-C, use [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) to free the dictionary’s memory when you are done with it.

#### Discussion

Call one of the [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) or [`SecTrustEvaluateAsyncWithError(_:_:_:)`](sectrustevaluateasyncwitherror(_:_:_:).md) methods before calling [`SecTrustCopyResult(_:)`](sectrustcopyresult(_:).md).

## Parameters

- `trust`: The evaluated trust.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcopyresult(_:))*