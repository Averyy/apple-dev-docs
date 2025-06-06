# getSpecific(key:)

**Framework**: Dispatch  
**Kind**: method

Returns the value for the key associated with this dispatch queue.

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
func getSpecific<T>(key: DispatchSpecificKey<T>) -> T? where T : Sendable
```

## Parameters

- `key`: The key associated with the dispatch queue.

## See Also

- [func setSpecific<T>(key: DispatchSpecificKey<T>, value: T?)](dispatchqueue/setspecific(key:value:).md)
  Sets the key/value data for the specified dispatch queue.
- [class func getSpecific<T>(key: DispatchSpecificKey<T>) -> T?](dispatchqueue/getspecific(key:)-swift.type.method.md)
  Returns the value for the key associated with the current execution context.
- [class DispatchSpecificKey](dispatchspecifickey.md)
  A key associated with a specific contextual value on a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/getspecific(key:)-swift.method)*