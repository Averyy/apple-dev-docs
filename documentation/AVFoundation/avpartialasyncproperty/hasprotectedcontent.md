# hasProtectedContent

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the asset contains protected content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var hasProtectedContent: AVAsyncProperty<Root, Bool> { get }
```

#### Discussion

Use the `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the property value.

Assets that contain protected content may not be playable without successful authorization, even if the value of its [`isPlayable`](avasset/isplayable.md) property is [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/hasprotectedcontent)*