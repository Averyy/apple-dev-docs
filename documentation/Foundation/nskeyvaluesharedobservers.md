# NSKeyValueSharedObservers

**Framework**: Foundation  
**Kind**: class

A collection of key-value observations which may be registered with multiple observable objects

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
class NSKeyValueSharedObservers
```

## Topics

### Initializers
- [init(observableClass: AnyClass)](nskeyvaluesharedobservers/init(observableclass:).md)
  A new collection of observables for an observable object of the given class
### Instance Methods
- [func addSharedObserver(NSObject, forKey: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nskeyvaluesharedobservers/addsharedobserver(_:forkey:options:context:).md)
  Add a new observer to the collection.
- [func snapshot() -> NSKeyValueSharedObserversSnapshot](nskeyvaluesharedobservers/snapshot.md)
  A momentary snapshot of all observers added to the collection thus far, that can be assigned to an observable using `-[NSObject setSharedObservers:]`

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSKeyValueObservation](nskeyvalueobservation.md)
- [class NSKeyValueSharedObserversSnapshot](nskeyvaluesharedobserverssnapshot.md)
  A collection of key-value observations which may be registered with multiple observable objects. Create using `-[NSKeyValueSharedObservers snapshot]`


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvaluesharedobservers)*