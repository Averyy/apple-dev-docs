# allowsNextDrawableTimeout

**Framework**: Core Animation  
**Kind**: property

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

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the [`nextDrawable()`](cametallayer/nextdrawable().md) method returns [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if it can’t provide a drawable object within one second. If [`false`](https://developer.apple.com/documentation/Swift/false), the [`nextDrawable()`](cametallayer/nextdrawable().md) method waits indefinitely for a drawable to become available.

The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [func nextDrawable() -> (any CAMetalDrawable)?](cametallayer/nextdrawable.md)
  Waits until a Metal drawable is available, and then returns it.
- [var maximumDrawableCount: Int](cametallayer/maximumdrawablecount.md)
  The number of Metal drawables in the resource pool managed by Core Animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/allowsnextdrawabletimeout)*