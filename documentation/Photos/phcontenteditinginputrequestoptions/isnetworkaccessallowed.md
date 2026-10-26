# isNetworkAccessAllowed

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether Photos can download the asset from iCloud.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isNetworkAccessAllowed: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isNetworkAccessAllowed) BOOL networkAccessAllowed;
```

#### Discussion

By default, the value is `false`. If `true`, Photos downloads the asset for editing if it’s not available on the local device. Use the [`progressHandler`](./progresshandler.md) property to track the progress of the download.

## See Also

### Fetching Asset Data from iCloud
- [var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Void)?](./progresshandler.md)
  A block Photos calls periodically while downloading the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions/isnetworkaccessallowed)*