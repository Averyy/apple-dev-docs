# PHLocalIdentifiersErrorKey

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

An error key that retrieves an array of string values representing local identifiers matched to a cloud identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
let PHLocalIdentifiersErrorKey: String
```

```c
extern NSErrorUserInfoKey const PHLocalIdentifiersErrorKey;
```

## Discussion

Use this key with the [`userInfo`](../Foundation/nserror/userinfo.md) property when encountering the [`multipleIdentifiersFound`](./phphotoserror-swift.struct/multipleidentifiersfound.md) error.

## See Also

### Inspecting an Error
- [static var errorDomain: String](./phphotoserror-swift.struct/errordomain.md)
- [PHPhotosError.Code](./phphotoserror-swift.struct/code.md)
  Error codes for framework operations.
- [Error Constants](../PhotoKit/error-constants.md)
  Error code constants for framework operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlocalidentifierserrorkey)*