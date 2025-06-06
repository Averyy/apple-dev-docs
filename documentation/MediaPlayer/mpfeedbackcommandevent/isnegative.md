# isNegative

**Framework**: Media Player  
**Kind**: property

A Boolean value that indicates whether an app should perform a negative command appropriate to the target.

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
var isNegative: Bool { get }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/swift/true), the designated element has a negative operation performed on the element. The performance of the `negative` command varies depending on the element it is referencing. For example, a `negative` command for a bookmark indicates that the bookmark should be removed. However, a `negative` command for a Like command could just lower the frequency that the designated element is played. This behavior differs from a Dislike command, which would put the designated element on a deny list and never play it again.

It’s up to the app to determine exactly what should be done when a `negative` command is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommandevent/isnegative)*