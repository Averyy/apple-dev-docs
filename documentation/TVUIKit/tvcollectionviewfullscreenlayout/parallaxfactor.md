# parallaxFactor

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

A value that specifies how slowly the background should move relative to the foreground.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var parallaxFactor: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat parallaxFactor;
```

## Discussion

A large `parallaxFactor` value causes the background to move more slowly compared to the foreground. A small value makes the foreground and background move at a similar pace. The parallax effect becomes more apparent as the value of `parallaxFactor` increases.

The default value of this property is 0.8. The minimum value is 0.0.

## See Also

### Managing transitions
- [var isTransitioningToCenterIndexPath: Bool](./istransitioningtocenterindexpath.md)
  A Boolean value that indicates whether the cell is changing index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreenlayout/parallaxfactor)*