# preservesDepth

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Defines whether this layer flattens its sublayers into its plane.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preservesDepth: Bool { get set }
```

```objc
@property BOOL preservesDepth;
```

#### Discussion

If [`true`](../../Swift/true.md), the layer acts similarly to the `CATransformLayer` and has the same restrictions.

Default is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer/preservesdepth)*