# AVKeyValueStatus

**Framework**: AVFoundation  
**Kind**: enum

Values that indicate the loaded status of a property.

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
enum AVKeyValueStatus
```

## Topics

### Status Values
- [AVKeyValueStatus.unknown](avkeyvaluestatus/unknown.md)
  The property value’s status is unknown.
- [AVKeyValueStatus.loading](avkeyvaluestatus/loading.md)
  The system is loading the property value.
- [AVKeyValueStatus.loaded](avkeyvaluestatus/loaded.md)
  The property value is ready to use.
- [AVKeyValueStatus.failed](avkeyvaluestatus/failed.md)
  The system is unable to load the propery value.
- [AVKeyValueStatus.cancelled](avkeyvaluestatus/cancelled.md)
  You canceled loading a property value.
### Initializers
- [init?(rawValue: Int)](avkeyvaluestatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Deprecated Symbols](avasynchronouskeyvalueloading-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
- [func loadValuesAsynchronously(forKeys: [String], completionHandler: (() -> Void)?)](avasynchronouskeyvalueloading/loadvaluesasynchronously(forkeys:completionhandler:).md)
  Tells the asset to load the values of all of the specified keys that aren’t already loaded.
- [func statusOfValue(forKey: String, error: NSErrorPointer) -> AVKeyValueStatus](avasynchronouskeyvalueloading/statusofvalue(forkey:error:).md)
  Returns a status that indicates whether a property value is immediately available without blocking the calling thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus)*