# NSCoder.DecodingFailurePolicy.raiseException

**Framework**: Foundation  
**Kind**: case

A failure policy that directs the coder to raise an exception.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case raiseException
```

#### Discussion

With this policy, the [`NSCoder`](nscoder.md) raises an exception internally to propagate failure messages (and unwind the stack). In Objective-C, this exception can be transformed into an [`NSError`](nserror.md) via methods like [`decodeTopLevelObjectAndReturnError:`](nscoder/decodetoplevelobjectandreturnerror:.md)

## See Also

- [NSCoder.DecodingFailurePolicy.setErrorAndReturn](nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn.md)
  A failure policy that directs the coder to capture the failure as an error object.
- [NSCoder.DecodingFailurePolicy.setErrorAndReturn](nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn.md)
  A failure policy that directs the coder to capture the failure as an error object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy-swift.enum/raiseexception)*