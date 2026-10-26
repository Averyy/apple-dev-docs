# BAManagedErrorCodeFileNotFound

**Framework**: Background Assets  
**Kind**: case  
**Role**: Enumeration Case

An error code that indicates the system couldn’t find a file at the specified path.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
BAManagedErrorCodeFileNotFound
```

#### Discussion

Refer to the value in `-[NSError userInfo]` for the key `NSFilePathErrorKey` for the file path.

## See Also

### Errors
- [BAManagedErrorCodeAssetPackNotFound](./bamanagederrorcodeassetpacknotfound.md)
  An error code that indicates the system couldn’t find an asset pack with the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/bamanagederrorcode/bamanagederrorcodefilenotfound)*