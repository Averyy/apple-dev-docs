# supportsURL(_:)

**Framework**: Safari Services  
**Kind**: method

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

#### Return Value

If [`true`](https://developer.apple.com/documentation/Swift/true), then the URL is supported by Reading List; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Use this method to determine whether to display a Reading List button in your app.

## Parameters

- `URL`: The URL to be tested for Reading List support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/ssreadinglist/supportsurl(_:))*