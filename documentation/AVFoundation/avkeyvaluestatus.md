# AVKeyValueStatus

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Values that indicate the loaded status of a property.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`AVAsyncProperty.Status`](./avasyncproperty/status.md) instead.

## Declaration

```swift
enum AVKeyValueStatus
```

```c
enum AVKeyValueStatus : NSInteger;
```

## Topics

### Status values
- [AVKeyValueStatus.unknown](./avkeyvaluestatus/unknown.md)
  The property value’s status is unknown.
- [AVKeyValueStatus.loading](./avkeyvaluestatus/loading.md)
  The system is loading the property value.
- [AVKeyValueStatus.loaded](./avkeyvaluestatus/loaded.md)
  The property value is ready to use.
- [AVKeyValueStatus.failed](./avkeyvaluestatus/failed.md)
  The system is unable to load the property value.
- [AVKeyValueStatus.cancelled](./avkeyvaluestatus/cancelled.md)
  You canceled loading a property value.
### Initializers
- [init?(rawValue: Int)](./avkeyvaluestatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [Deprecated symbols](./avasynchronouskeyvalueloading-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
- [func loadValuesAsynchronously(forKeys: [String], completionHandler: (() -> Void)?)](./avasynchronouskeyvalueloading/loadvaluesasynchronously%28forkeys,completionhandler%29.md)
  Tells the asset to load the values of all of the specified keys that aren’t already loaded.
- [func statusOfValue(forKey: String, error: NSErrorPointer) -> AVKeyValueStatus](./avasynchronouskeyvalueloading/statusofvalue%28forkey,error%29.md)
  Returns a status that indicates whether a property value is immediately available without blocking the calling thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avkeyvaluestatus)*