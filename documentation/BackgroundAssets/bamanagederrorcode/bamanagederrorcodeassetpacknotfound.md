# BAManagedErrorCodeAssetPackNotFound

**Framework**: Background Assets  
**Kind**: case  
**Role**: Enumeration Case

An error code that indicates the system couldn’t find an asset pack with the given identifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
BAManagedErrorCodeAssetPackNotFound
```

## Discussion

Refer to the value in `-[NSError userInfo]` for the key [`BAAssetPackIdentifierErrorKey`](../baassetpackidentifiererrorkey.md) for the asset pack’s identifier.

## See Also

### Errors
- [BAManagedErrorCodeFileNotFound](./bamanagederrorcodefilenotfound.md)
  An error code that indicates the system couldn’t find a file at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/bamanagederrorcode/bamanagederrorcodeassetpacknotfound)*