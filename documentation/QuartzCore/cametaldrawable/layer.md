# layer

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The layer that owns this drawable object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var layer: CAMetalLayer { get }
```

```objc
@property (readonly) CAMetalLayer * layer;
```

#### Discussion

When you present the drawable object, it becomes the owning layer’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldrawable/layer)*