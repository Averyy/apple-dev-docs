# copiesOnScroll

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the clip view copies rendered images while scrolling.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var copiesOnScroll: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the clip view copies its existing rendered image while scrolling (only drawing exposed portions of its document view); when it is [`false`](https://developer.apple.com/documentation/Swift/false), the view forces its contents to be redrawn each time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/copiesonscroll)*