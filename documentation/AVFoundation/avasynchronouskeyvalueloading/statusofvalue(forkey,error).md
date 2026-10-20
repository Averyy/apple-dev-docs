# statusOfValue(forKey:error:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a status that indicates whether a property value is immediately available without blocking the calling thread.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`status(of:)`](./status%28of%29.md) instead.

## Declaration

```swift
func statusOfValue(forKey key: String, error outError: NSErrorPointer) -> AVKeyValueStatus
```

```objc
- (AVKeyValueStatus) statusOfValueForKey:(NSString *) key error:(NSError **) outError;
```

#### Return Value

The current status of the requested key.

## Parameters

- `key`: The property whose status you want.
- `outError`: If the status of the value for the `key` is [`AVKeyValueStatus.failed`](../avkeyvaluestatus/failed.md), the system sets this pointer to an [`NSError`](../../Foundation/nserror.md) object that describes the failure.

## See Also

### Deprecated
- [Deprecated symbols](../avasynchronouskeyvalueloading-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
- [func loadValuesAsynchronously(forKeys: [String], completionHandler: (() -> Void)?)](./loadvaluesasynchronously%28forkeys,completionhandler%29.md)
  Tells the asset to load the values of all of the specified keys that aren’t already loaded.
- [enum AVKeyValueStatus](../avkeyvaluestatus.md)
  Values that indicate the loaded status of a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/statusofvalue(forkey:error:))*