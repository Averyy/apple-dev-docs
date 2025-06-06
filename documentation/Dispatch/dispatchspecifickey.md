# DispatchSpecificKey

**Framework**: Dispatch  
**Kind**: class

A key associated with a specific contextual value on a dispatch queue.

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
final class DispatchSpecificKey<T>
```

#### Overview

Access the value of a key using the [`setSpecific(key:value:)`](dispatchqueue/setspecific(key:value:).md) and [`getSpecific(key:)`](dispatchqueue/getspecific(key:)-swift.method.md) methods.

## Topics

### Creating a Key
- [init()](dispatchspecifickey/init.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setSpecific<T>(key: DispatchSpecificKey<T>, value: T?)](dispatchqueue/setspecific(key:value:).md)
  Sets the key/value data for the specified dispatch queue.
- [func getSpecific<T>(key: DispatchSpecificKey<T>) -> T?](dispatchqueue/getspecific(key:)-swift.method.md)
  Returns the value for the key associated with this dispatch queue.
- [class func getSpecific<T>(key: DispatchSpecificKey<T>) -> T?](dispatchqueue/getspecific(key:)-swift.type.method.md)
  Returns the value for the key associated with the current execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchspecifickey)*