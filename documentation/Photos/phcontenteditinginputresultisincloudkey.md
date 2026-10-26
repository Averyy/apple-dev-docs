# PHContentEditingInputResultIsInCloudKey

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

A Boolean value indicating whether the asset data is stored on the local device or must be downloaded from iCloud. (`NSNumber`)

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let PHContentEditingInputResultIsInCloudKey: String
```

```c
extern NSString * const PHContentEditingInputResultIsInCloudKey;
```

#### Discussion

If `true`, no asset data was provided because the asset data must be downloaded from iCloud. To do this, submit another request, specifying `true` for the [`isNetworkAccessAllowed`](./phcontenteditinginputrequestoptions/isnetworkaccessallowed.md) option.

## See Also

### Constants
- [let PHContentEditingInputCancelledKey: String](./phcontenteditinginputcancelledkey.md)
  A Boolean value indicating whether the image request was canceled. (`NSNumber`)
- [let PHContentEditingInputErrorKey: String](./phcontenteditinginputerrorkey.md)
  An error that occurred while attempting to load the asset data. (`NSError`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginputresultisincloudkey)*