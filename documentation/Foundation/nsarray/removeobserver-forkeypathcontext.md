# removeObserver(_:forKeyPath:context:)

**Framework**: Foundation  
**Kind**: method

Raises an exception.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context: UnsafeMutableRawPointer?)
```

#### Discussion

`NSArray` objects are not observable, so this method raises an exception when invoked on an `NSArray` object. Instead of observing a array, observe the ordered to-many relationship for which the array is the collection of related objects.

## Parameters

- `observer`: The object to remove as an observer.
- `keyPath`: A key-path, relative to the set, for which   is registered to receive KVO change notifications. This value must not be  .
- `context`: The context passed to the notifications.

## See Also

- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsarray/addobserver(_:forkeypath:options:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](nsarray/removeobserver(_:forkeypath:).md)
  Raises an exception.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsarray/removeobserver(_:fromobjectsat:forkeypath:context:).md)
  Raises an exception.
- [func addObserver(NSObject, toObjectsAt: IndexSet, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsarray/addobserver(_:toobjectsat:forkeypath:options:context:).md)
  Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String)](nsarray/removeobserver(_:fromobjectsat:forkeypath:).md)
  Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/removeobserver(_:forkeypath:context:))*