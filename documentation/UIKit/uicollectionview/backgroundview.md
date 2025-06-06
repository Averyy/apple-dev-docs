# backgroundView

**Framework**: UIKit  
**Kind**: property

The view that provides the background appearance.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var backgroundView: UIView? { get set }
```

#### Discussion

The view (if any) in this property is positioned underneath all of the other content and sized automatically to fill the entire bounds of the collection view. The background view does not scroll with the collection view’s other content. The collection view maintains a strong reference to the background view object.

This property is `nil` by default, which displays the background color of the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/backgroundview)*