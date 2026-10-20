# DispatchSpecificKey

**Framework**: Dispatch  
**Kind**: class  
**Role**: Class

A key associated with a specific contextual value on a dispatch queue.

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
final class DispatchSpecificKey<T>
```

#### Overview

Access the value of a key using the [`setSpecific(key:value:)`](./dispatchqueue/setspecific%28key,value%29.md) and [`getSpecific(key:)`](./dispatchqueue/getspecific%28key%29-swift.method.md) methods.

## Topics

### Creating a Key
- [init()](./dispatchspecifickey/init%28%29.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting and Setting Contextual Data
- [func setSpecific<T>(key: DispatchSpecificKey<T>, value: T?)](./dispatchqueue/setspecific%28key,value%29.md)
  Sets the key/value data for the specified dispatch queue.
- [func getSpecific<T>(key: DispatchSpecificKey<T>) -> T?](./dispatchqueue/getspecific%28key%29-swift.method.md)
  Returns the value for the key associated with this dispatch queue.
- [class func getSpecific<T>(key: DispatchSpecificKey<T>) -> T?](./dispatchqueue/getspecific%28key%29-swift.type.method.md)
  Returns the value for the key associated with the current execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchspecifickey)*