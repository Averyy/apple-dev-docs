# init(shareURLs:)

**Framework**: CloudKit  
**Kind**: init

Creates a [`CKShareRequestAccessOperation`](cksharerequestaccessoperation.md) for requesting access to the specified shares.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
convenience init(shareURLs: [URL])
```

#### Return Value

A [`CKShareRequestAccessOperation`](cksharerequestaccessoperation.md) instance configured with the given share URLs.

## Parameters

- `shareURLs`: An array of   objects for shares you wish to request access to


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation/init(shareurls:))*