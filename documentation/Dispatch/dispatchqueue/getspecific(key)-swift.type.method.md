# getSpecific(key:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Type Method

Returns the value for the key associated with the current execution context.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
@preconcurrency
class func getSpecific<T>(key: DispatchSpecificKey<T>) -> T? where T : Sendable
```

## Parameters

- `key`: The key associated with the dispatch queue.

## See Also

### Getting and Setting Contextual Data
- [func setSpecific<T>(key: DispatchSpecificKey<T>, value: T?)](./setspecific%28key,value%29.md)
  Sets the key/value data for the specified dispatch queue.
- [func getSpecific<T>(key: DispatchSpecificKey<T>) -> T?](./getspecific%28key%29-swift.method.md)
  Returns the value for the key associated with this dispatch queue.
- [class DispatchSpecificKey](../dispatchspecifickey.md)
  A key associated with a specific contextual value on a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/getspecific(key:)-swift.type.method)*