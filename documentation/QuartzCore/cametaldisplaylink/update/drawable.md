# drawable

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The Metal drawable your app uses to render the next frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var drawable: any CAMetalDrawable { get }
```

```objc
@property (nonatomic, readonly) id<CAMetalDrawable> drawable;
```

## See Also

### Drawing the Next Frame
- [var targetTimestamp: CFTimeInterval](./targettimestamp.md)
  A deadline that indicates when your app needs to finish rendering to the drawable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/update/drawable)*