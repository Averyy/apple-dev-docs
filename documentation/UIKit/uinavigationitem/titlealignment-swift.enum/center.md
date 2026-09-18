# UINavigationItem.TitleAlignment.center

**Framework**: UIKit  
**Kind**: case

The title is center-aligned.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)

## Declaration

```swift
case center
```

#### Discussion

Unlike Automatic, this never falls back to leading alignment: a title that cannot be centered shifts toward the leading edge to clear the trailing bar content, and truncates only once it can shift no further.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/titlealignment-swift.enum/center)*