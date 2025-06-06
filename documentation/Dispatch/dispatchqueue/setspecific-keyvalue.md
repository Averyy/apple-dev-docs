# setSpecific(key:value:)

**Framework**: Dispatch  
**Kind**: method

Sets the key/value data for the specified dispatch queue.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@preconcurrency
func setSpecific<T>(key: DispatchSpecificKey<T>, value: T?) where T : Sendable
```

## Parameters

- `key`: The key that you use to identify the data.
- `value`: The data you want to associate with the queue.

## See Also

- [func getSpecific<T>(key: DispatchSpecificKey<T>) -> T?](dispatchqueue/getspecific(key:)-swift.method.md)
  Returns the value for the key associated with this dispatch queue.
- [class func getSpecific<T>(key: DispatchSpecificKey<T>) -> T?](dispatchqueue/getspecific(key:)-swift.type.method.md)
  Returns the value for the key associated with the current execution context.
- [class DispatchSpecificKey](dispatchspecifickey.md)
  A key associated with a specific contextual value on a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/setspecific(key:value:))*