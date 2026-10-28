# SecTrustSetExceptions(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets a list of exceptions that should be ignored when the certificate is evaluated.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecTrustSetExceptions(_ trust: SecTrust, _ exceptions: CFData?) -> Bool
```

```c
bool SecTrustSetExceptions(SecTrustRef trust, CFDataRef exceptions);
```

## Return Value

A Boolean that is [`true`](../Swift/true.md) if the exceptions cookies was valid and matches the current leaf certificate, [`false`](../Swift/false.md) otherwise.

## Discussion

> ❗ **Important**: Even if this function returns true, you must still call [`SecTrustEvaluateWithError(_:_:)`](./sectrustevaluatewitherror%28_,_%29.md) because the evaluation can still fail if something changes between the initial evaluation and the reevaluation.

## Parameters

- `trust`: The trust management object whose exception list you wish to modify.
- `exceptions`: An opaque cookie returned by a prior call to [`SecTrustCopyExceptions(_:)`](./sectrustcopyexceptions%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsetexceptions(_:_:))*