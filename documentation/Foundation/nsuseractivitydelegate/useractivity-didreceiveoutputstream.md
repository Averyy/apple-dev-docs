# userActivity(_:didReceive:outputStream:)

**Framework**: Foundation  
**Kind**: method

Notifies the user activity delegate that an input and output streams are available to open.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func userActivity(_ userActivity: NSUserActivity, didReceive inputStream: InputStream, outputStream: OutputStream)
```

#### Discussion

If [`supportsContinuationStreams`](nsuseractivity/supportscontinuationstreams.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the continuing app can request streams back to the originating app. This delegate callback is received with the streams from the continuing side. The streams are provided in an unopened state, and the delegate should open them immediately to start communicating with the continuing side.

Continuation streams are an optional feature of Handoff, and most user activities do not need them for successful continuation. When streams are needed, a simple request from the continuing app accompanied by a response from the originating app is enough for most continuation events.

## Parameters

- `userActivity`: The user activity that is continuing on another device. This user activity’s   property must be  .
- `inputStream`: The stream from which the originating app can read data written from the continuing app.
- `outputStream`: The stream to which the originating app writes data to be read by the continuing app.

## See Also

- [Handoff Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Handoff/HandoffFundamentals/HandoffFundamentals.html#//apple_ref/doc/uid/TP40014338)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/useractivity(_:didreceive:outputstream:))*