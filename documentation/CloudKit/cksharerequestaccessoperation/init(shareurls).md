# init(shareURLs:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a share request access operation configured with specified share URLs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
convenience init(shareURLs: [URL])
```

```objc
- (instancetype) initWithShareURLs:(NSArray<NSURL *> *) shareURLs;
```

#### Return Value

A configured [`CKShareRequestAccessOperation`](../cksharerequestaccessoperation.md) instance.

## Parameters

- `shareURLs`: An array of `NSURL` objects representing the shares to request access to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation/init(shareurls:))*