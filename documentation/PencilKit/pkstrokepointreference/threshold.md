# threshold

**Framework**: PencilKit  
**Kind**: property

The alpha threshold for clipping the stroke rendering for supported inks.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var threshold: CGFloat { get }
```

#### Discussion

Only pixels with an alpha greater than the threshold are drawn. A threshold of `0` has no effect on rendering; a threshold of `1` draws nothing. Thresholds apply only to some inks, such as `PKInkIdentifierReed`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepointreference/threshold)*