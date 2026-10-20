# contentKeySession(_:didProvide:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the recipient that a content key is available.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
optional func contentKeySession(_ contentKeySession: AVContentKeySession, didProvide contentKey: AVContentKey)
```

```objc
- (void) contentKeySession:(AVContentKeySession *) contentKeySession didProvideContentKey:(AVContentKey *) contentKey;
```

## Parameters

- `contentKeySession`: The current content key session.
- `contentKey`: A content key to use with objects that support manual attachment of keys, such as [`CMSampleBuffer`](../../CoreMedia/cmsamplebuffer.md).

## See Also

### Verifying decryption key requirements
- [var mayRequireContentKeysForMediaDataProcessing: Bool](./mayrequirecontentkeysformediadataprocessing.md)
  A Boolean value that indicates whether the recipient requires decryption keys for media data to enable processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrecipient/contentkeysession(_:didprovide:))*