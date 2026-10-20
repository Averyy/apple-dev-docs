# isIncremental

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the request provides data incrementally.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

## Declaration

```swift
var isIncremental: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isIncremental) BOOL incremental;
```

#### Discussion

Before adding or removing any entries, if you call this method and the value is [`true`](../../Swift/true.md), the request must only add or remove entries relative to the last time the system loaded data for the extension. Otherwise, if you don’t call this method, or if the value is [`false`](../../Swift/false.md), the request must add the full list of entries without removing any, regardless of whether the system loaded data in the past.

## See Also

### Completing Requests
- [func completeRequest(completionHandler: ((Bool) -> Void)?)](./completerequest%28completionhandler%29.md)
  Completes the request to the extension context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/isincremental)*