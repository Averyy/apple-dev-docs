# aspectRatio

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The content’s aspect ratio.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var aspectRatio: CGFloat { get set }
```

```objc
@property (nonatomic, readwrite) CGFloat aspectRatio;
```

#### Discussion

This property represents the ratio of the content’s width to its height. The value of this property must be greater than `0.0` and less than or equal to `100.0`. The default value is `1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguideaspectfitting/aspectratio)*