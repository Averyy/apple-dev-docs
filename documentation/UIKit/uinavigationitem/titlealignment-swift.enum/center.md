# UINavigationItem.TitleAlignment.center

**Framework**: UIKit  
**Kind**: case

The title is center-aligned.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- tvOS 27.2+
- visionOS 27.2+

## Declaration

```swift
case center
```

#### Discussion

Unlike Automatic, this never falls back to leading alignment: a title that cannot be centered shifts toward the leading edge to clear the trailing bar content, and truncates only once it can shift no further.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/titlealignment-swift.enum/center)*