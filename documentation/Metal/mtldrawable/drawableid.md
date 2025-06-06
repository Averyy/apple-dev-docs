# drawableID

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A positive integer that identifies the drawable.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var drawableID: Int { get }
```

#### Discussion

Drawable objects are usually owned by some other object, such as a [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer). The owning object gives the first drawable it creates an ID of `0`, and it increments the ID by `1` for each additional drawable it creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawable/drawableid)*