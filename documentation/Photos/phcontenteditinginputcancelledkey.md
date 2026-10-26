# PHContentEditingInputCancelledKey

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

A Boolean value indicating whether the image request was canceled. (`NSNumber`)

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let PHContentEditingInputCancelledKey: String
```

```c
extern NSString * const PHContentEditingInputCancelledKey;
```

#### Discussion

If you call the [`cancelContentEditingInputRequest(_:)`](./phasset/cancelcontenteditinginputrequest%28_%29.md) method to cancel a request, Photos calls your result handler block with the value `true` for this key.

## See Also

### Constants
- [let PHContentEditingInputResultIsInCloudKey: String](./phcontenteditinginputresultisincloudkey.md)
  A Boolean value indicating whether the asset data is stored on the local device or must be downloaded from iCloud. (`NSNumber`)
- [let PHContentEditingInputErrorKey: String](./phcontenteditinginputerrorkey.md)
  An error that occurred while attempting to load the asset data. (`NSError`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginputcancelledkey)*