# handle

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The handle of the call recipient.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@NSCopying
var handle: CXHandle { get set }
```

```objc
@property (nonatomic, copy) CXHandle * handle;
```

## See Also

### Accessing Action Attributes
- [var isVideo: Bool](./isvideo.md)
  A Boolean value that indicates whether the call is a video call.
- [var contactIdentifier: String?](./contactidentifier.md)
  The identifier for the call recipient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxstartcallaction/handle)*