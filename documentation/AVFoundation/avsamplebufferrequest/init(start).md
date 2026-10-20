# init(start:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a newly allocated sample buffer request with the specified sample cursor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.10+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(start startCursor: AVSampleCursor)
```

```objc
- (instancetype) initWithStartCursor:(AVSampleCursor *) startCursor;
```

#### Return Value

An initialized `AVSampleBufferRequest` instance.

## Parameters

- `startCursor`: The starting cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/init(start:))*