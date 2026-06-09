# barMinimizeBehavior

**Framework**: UIKit  
**Kind**: property

The minimize behavior for the navigation bar.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var barMinimizeBehavior: UIBarMinimizeBehavior { get set }
```

#### Discussion

The default value is [`UIBarMinimizeBehavior.automatic`](uibarminimizebehavior/automatic.md). When the navigation bar minimizes, an integrated top tab bar will also minimize.

By default, the safe area adjusts as the navigation bar minimizes. Use [`barMinimizationSafeAreaAdjustment`](uinavigationitem/barminimizationsafeareaadjustment.md) to customize this.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/barminimizebehavior)*