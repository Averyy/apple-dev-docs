# isIncremental

**Framework**: CallKit  
**Kind**: property

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

#### Discussion

Before adding or removing any entries, if you call this method and the value is [`true`](https://developer.apple.com/documentation/Swift/true), the request must only add or remove entries relative to the last time the system loaded data for the extension. Otherwise, if you don’t call this method, or if the value is [`false`](https://developer.apple.com/documentation/Swift/false), the request must add the full list of entries without removing any, regardless of whether the system loaded data in the past.

## See Also

- [func completeRequest(completionHandler: ((Bool) -> Void)?)](cxcalldirectoryextensioncontext/completerequest(completionhandler:).md)
  Completes the request to the extension context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext/isincremental)*