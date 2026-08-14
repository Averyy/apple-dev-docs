# isEnabled

**Framework**: Media Player  
**Kind**: property

A Boolean value that indicates whether a user can interact with the displayed element.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/swift/true), the designated element is enabled so users can interact with it. When set to [`false`](https://developer.apple.com/documentation/swift/false), events for this command are not sent to your app, and the user interface may be changed to reflect this when your app is the Now Playing app. The default value is [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/isenabled)*