# hasProtectedContent

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the asset contains protected content.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+

## Declaration

```swift
var hasProtectedContent: Bool { get }
```

#### Discussion

Assets that contain protected content may not be playable without successful authorization, even if the value of its [`isPlayable`](avasset/isplayable.md) property is [`true`](https://developer.apple.com/documentation/Swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/hasprotectedcontent)*