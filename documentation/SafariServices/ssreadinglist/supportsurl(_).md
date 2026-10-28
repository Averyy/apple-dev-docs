# supportsURL(_:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Type Method

Determines whether a URL can be added to the Reading List.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class func supportsURL(_ URL: URL) -> Bool
```

```objc
+ (BOOL) supportsURL:(NSURL *) URL;
```

## Return Value

If [`true`](../../Swift/true.md), then the URL is supported by Reading List; otherwise, [`false`](../../Swift/false.md).

## Discussion

Use this method to determine whether to display a Reading List button in your app.

## Parameters

- `URL`: The URL to be tested for Reading List support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/ssreadinglist/supportsurl(_:))*