# PHContentEditingInputErrorKey

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

An error that occurred while attempting to load the asset data. (`NSError`)

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let PHContentEditingInputErrorKey: String
```

```c
extern NSString * const PHContentEditingInputErrorKey;
```

#### Discussion

Photos provides an error object for this key if it cannot provide asset data for your handler block’s `contentEditingInput` parameter. Examine the error object for information about the cause of the error.

## See Also

### Constants
- [let PHContentEditingInputResultIsInCloudKey: String](./phcontenteditinginputresultisincloudkey.md)
  A Boolean value indicating whether the asset data is stored on the local device or must be downloaded from iCloud. (`NSNumber`)
- [let PHContentEditingInputCancelledKey: String](./phcontenteditinginputcancelledkey.md)
  A Boolean value indicating whether the image request was canceled. (`NSNumber`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginputerrorkey)*