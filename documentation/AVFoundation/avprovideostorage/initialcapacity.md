# initialCapacity

**Framework**: AVFoundation  
**Kind**: property

Initial size of Pro Video Storage in bytes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var initialCapacity: Int { get }
```

#### Return Value

0 if Pro Video Storage is not configured or -1 if there was a failure while extracting information from it.

#### Discussion

The initial capacity is defined by the user via the Settings app.

## See Also

- [var remainingCapacity: Int](avprovideostorage/remainingcapacity.md)
  Current size of Pro Video Storage in bytes.
- [func replenishCapacity(completionHandler: ((Int, (any Error)?) -> Void)?)](avprovideostorage/replenishcapacity(completionhandler:).md)
  Performs a best-effort attempt to restore Pro Video Storage to the initial capacity specified by the user in Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage/initialcapacity)*