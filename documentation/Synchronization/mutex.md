# Mutex

**Framework**: Synchronization  
**Kind**: struct

A synchronization primitive that protects shared mutable state via mutual exclusion.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
struct Mutex<Value> where Value : ~Copyable
```

#### Overview

The `Mutex` type offers non-recursive exclusive access to the state it is protecting by blocking threads attempting to acquire the lock. Only one execution context at a time has access to the value stored within the `Mutex` allowing for exclusive access.

An example use of `Mutex` in a class used simultaneously by many threads protecting a `Dictionary` value:

```swift
class Manager {
  let cache = Mutex<[Key: Resource]>([:])

  func saveResource(_ resource: Resource, as key: Key) {
    cache.withLock {
      $0[key] = resource
    }
  }
}
```

## Topics

### Initializers
- [init(consuming sending Value)](mutex/init(_:).md)
  Initializes a value of this mutex with the given initial state.
### Instance Methods
- [func withLock<Result, E>((inout sending Value) throws(E) -> sending Result) throws(E) -> sending Result](mutex/withlock(_:).md)
  Calls the given closure after acquiring the lock and then releases ownership.
- [func withLockIfAvailable<Result, E>((inout sending Value) throws(E) -> sending Result) throws(E) -> sending Result?](mutex/withlockifavailable(_:).md)
  Attempts to acquire the lock and then calls the given closure if successful.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/mutex)*