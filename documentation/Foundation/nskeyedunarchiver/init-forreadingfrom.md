# init(forReadingFrom:)

**Framework**: Foundation  
**Kind**: init

Initializes an archiver to decode data from the specified location.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(forReadingFrom data: Data) throws
```

#### Discussion

This initializer enables [`requiresSecureCoding`](nskeyedunarchiver/requiressecurecoding.md) by default, and sets the [`decodingFailurePolicy`](nskeyedunarchiver/decodingfailurepolicy.md) to [`NSCoder.DecodingFailurePolicy.setErrorAndReturn`](nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn.md).

Call [`finishDecoding()`](nskeyedunarchiver/finishdecoding().md) when you finish decoding data

This method throws an error if `data` isn’t a valid keyed archive.

> ❗ **Important**:  If you are adapting existing code to use this initializer, make sure you have adopted [`NSSecureCoding`](nssecurecoding.md) in the types you decode. If any call to a `decode`-prefixed method fails, the default [`decodingFailurePolicy`](nskeyedunarchiver/decodingfailurepolicy.md) sets the [`error`](nscoder/error.md) rather than throwing an exception. In this case, the current and all subsequent decode calls return `0` or `nil`.

 If you are adapting existing code to use this initializer, make sure you have adopted [`NSSecureCoding`](nssecurecoding.md) in the types you decode. If any call to a `decode`-prefixed method fails, the default [`decodingFailurePolicy`](nskeyedunarchiver/decodingfailurepolicy.md) sets the [`error`](nscoder/error.md) rather than throwing an exception. In this case, the current and all subsequent decode calls return `0` or `nil`.

## Parameters

- `data`: An archive previously encoded by  .

## See Also

- [init()](nskeyedunarchiver/init.md)
  Initializes an archiver to decode data.
- [init(forReadingWith: Data)](nskeyedunarchiver/init(forreadingwith:).md)
  Initializes an archiver to decode data from the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/init(forreadingfrom:))*