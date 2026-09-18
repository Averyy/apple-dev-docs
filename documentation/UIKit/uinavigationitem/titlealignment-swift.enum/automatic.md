# UINavigationItem.TitleAlignment.automatic

**Framework**: UIKit  
**Kind**: case

The system determines the alignment.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)

## Declaration

```swift
case automatic
```

#### Discussion

Typically, the title is centered, but the system may choose to leading align the title based on the context the title is rendered in. When read from `UITraitCollection.navigationTitleAlignment`, this means the system has not resolved an alignment for the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/titlealignment-swift.enum/automatic)*