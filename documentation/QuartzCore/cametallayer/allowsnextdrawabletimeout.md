# allowsNextDrawableTimeout

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether requests for a new buffer expire if the system can’t satisfy them.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var allowsNextDrawableTimeout: Bool { get set }
```

```objc
@property BOOL allowsNextDrawableTimeout;
```

#### Discussion

If [`true`](../../Swift/true.md), the [`nextDrawable()`](./nextdrawable%28%29.md) method returns [`nil`](../../ObjectiveC/nil-227m0.md) if it can’t provide a drawable object within one second. If [`false`](../../Swift/false.md), the [`nextDrawable()`](./nextdrawable%28%29.md) method waits indefinitely for a drawable to become available.

The default value is [`true`](../../Swift/true.md).

## See Also

### Obtaining a Metal Drawable
- [func nextDrawable() -> (any CAMetalDrawable)?](./nextdrawable%28%29.md)
  Waits until a Metal drawable is available, and then returns it.
- [var maximumDrawableCount: Int](./maximumdrawablecount.md)
  The number of Metal drawables in the resource pool managed by Core Animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/allowsnextdrawabletimeout)*