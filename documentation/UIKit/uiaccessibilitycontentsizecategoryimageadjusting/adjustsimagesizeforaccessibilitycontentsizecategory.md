# adjustsImageSizeForAccessibilityContentSizeCategory

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the image size increases to support accessibility content size categories.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var adjustsImageSizeForAccessibilityContentSizeCategory: Bool { get set }
```

```objc
@property (nonatomic) BOOL adjustsImageSizeForAccessibilityContentSizeCategory;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the current object scales its image to an appropriate accessibility content size category. When the value of this property is [`false`](../../Swift/false.md), the current object displays its image at the regular content sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontentsizecategoryimageadjusting/adjustsimagesizeforaccessibilitycontentsizecategory)*