# remainingCapacity

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Current size of Pro Video Storage in bytes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var remainingCapacity: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger remainingCapacity;
```

#### Return Value

0 if Pro Video Storage is not configured or -1 if there was a failure while extracting information from it.

#### Discussion

The remaining capacity decreases as recordings are captured.

## See Also

### Inspecting capacity
- [var initialCapacity: Int](./initialcapacity.md)
  Initial size of Pro Video Storage in bytes.
- [func replenishCapacity(completionHandler: ((Int, (any Error)?) -> Void)?)](./replenishcapacity%28completionhandler%29.md)
  Performs a best-effort attempt to restore Pro Video Storage to the initial capacity specified by the user in Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage/remainingcapacity)*