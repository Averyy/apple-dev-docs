# NSKeyValueSharedObservers

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSKeyValueSharedObservers : NSObject
```

## Topics

### Initializers
- [init(observableClass: AnyClass)](./nskeyvaluesharedobservers/init%28observableclass%29.md)
  A new collection of observables for an observable object of the given class
### Instance Methods
- [func addSharedObserver(NSObject, forKey: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./nskeyvaluesharedobservers/addsharedobserver%28_,forkey,options,context%29.md)
  Add a new observer to the collection.
- [func snapshot() -> NSKeyValueSharedObserversSnapshot](./nskeyvaluesharedobservers/snapshot%28%29.md)
  A momentary snapshot of all observers added to the collection thus far, that can be assigned to an observable using `-[NSObject setSharedObservers:]`

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
- [class NSKeyValueObservation](./nskeyvalueobservation.md)
- [class NSKeyValueSharedObserversSnapshot](./nskeyvaluesharedobserverssnapshot.md)
  A collection of key-value observations which may be registered with multiple observable objects. Create using `-[NSKeyValueSharedObservers snapshot]`


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvaluesharedobservers)*