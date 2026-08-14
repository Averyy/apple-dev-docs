# statusOfValue(forKey:error:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Returns a status that indicates whether a property value is immediately available without blocking the calling thread.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func statusOfValue(forKey key: String, error outError: NSErrorPointer) -> AVKeyValueStatus
```

#### Return Value

The current status of the requested key.

## Parameters

- `key`: The property whose status you want.
- `outError`: If the status of the value for the `key` is [`AVKeyValueStatus.failed`](avkeyvaluestatus/failed.md), the system sets this pointer to an [`NSError`](https://developer.apple.com/documentation/foundation/nserror) object that describes the failure.

## See Also

- [Deprecated symbols](avasynchronouskeyvalueloading-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
- [func loadValuesAsynchronously(forKeys: [String], completionHandler: (() -> Void)?)](avasynchronouskeyvalueloading/loadvaluesasynchronously(forkeys:completionhandler:).md)
  Tells the asset to load the values of all of the specified keys that aren’t already loaded.
- [enum AVKeyValueStatus](avkeyvaluestatus.md)
  Values that indicate the loaded status of a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/statusofvalue(forkey:error:))*