# captureStreams()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Completes any already enqueued reads and writes, and then invokes the [`urlSession(_:streamTask:didBecome:outputStream:)`](../urlsessionstreamdelegate/urlsession%28_,streamtask,didbecome,outputstream%29.md) delegate message.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func captureStreams()
```

```objc
- (void) captureStreams;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/capturestreams())*