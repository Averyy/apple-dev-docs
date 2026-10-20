# isPlayable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the asset has playable content.

**Availability**:
- iOS 4.3+ - Deprecated in 16.0
- iPadOS 4.3+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`isPlayable`](../avpartialasyncproperty/isplayable-45h5v.md) asynchronously instead.

## Declaration

```swift
var isPlayable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPlayable) BOOL playable;
```

#### Discussion

This property value is [`true`](../../Swift/true.md) if you can use the asset to create an [`AVPlayerItem`](../avplayeritem.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/isplayable)*