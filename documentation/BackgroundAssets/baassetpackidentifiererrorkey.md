# BAAssetPackIdentifierErrorKey

**Framework**: Background Assets  
**Kind**: var  
**Role**: Global Variable

The `-[NSError userInfo]` key for an asset pack’s identifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
extern NSErrorUserInfoKey const BAAssetPackIdentifierErrorKey;
```

#### Discussion

This key is relevant when the error code is [`BAManagedErrorCodeAssetPackNotFound`](./bamanagederrorcode/bamanagederrorcodeassetpacknotfound.md). Its value should be an `NSString` object.

## See Also

### Errors
- [BAManagedErrorDomain](./bamanagederrordomain.md)
  The error domain for managed asset packs.
- [BAManagedErrorCode](./bamanagederrorcode.md)
  An error code for a managed asset pack.
- [let BAErrorDomain: String](./baerrordomain.md)
- [enum BAErrorCode](./baerrorcode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackidentifiererrorkey)*