# isComposable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can use the asset as a segment of a composition track.

**Availability**:
- iOS 4.3+ - Deprecated in 16.0
- iPadOS 4.3+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`isComposable`](../avpartialasyncproperty/iscomposable.md) asynchronously instead.

## Declaration

```swift
var isComposable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isComposable) BOOL composable;
```

#### Discussion

This property value is [`true`](../../Swift/true.md) you can use the asset as a segment within an [`AVCompositionTrack`](../avcompositiontrack.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/iscomposable)*