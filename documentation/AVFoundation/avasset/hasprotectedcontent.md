# hasProtectedContent

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the asset contains protected content.

**Availability**:
- iOS 4.2+ - Deprecated in 16.0
- iPadOS 4.2+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0

> **Deprecated**: Load the value of [`hasProtectedContent`](../avpartialasyncproperty/hasprotectedcontent.md) asynchronously instead.

## Declaration

```swift
var hasProtectedContent: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasProtectedContent;
```

## Discussion

Assets that contain protected content may not be playable without successful authorization, even if the value of its [`isPlayable`](./isplayable.md) property is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/hasprotectedcontent)*