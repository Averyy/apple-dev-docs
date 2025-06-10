# removeObserver(_:fromObjectsAt:forKeyPath:)

**Framework**: Foundation  
**Kind**: method

Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeObserver(_ observer: NSObject, fromObjectsAt indexes: IndexSet, forKeyPath keyPath: String)
```

#### Discussion

This is not merely a convenience method; invoking this method is potentially much faster than repeatedly invoking doc://com.apple.documentation/documentation/objectivec/nsobject/1408054-removeobserver.

## Parameters

- `observer`: The observer.
- `indexes`: The index set.
- `keyPath`: The key path, relative to the array, to be observed.

## See Also

- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsarray/addobserver(_:forkeypath:options:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](nsarray/removeobserver(_:forkeypath:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsarray/removeobserver(_:forkeypath:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsarray/removeobserver(_:fromobjectsat:forkeypath:context:).md)
  Raises an exception.
- [func addObserver(NSObject, toObjectsAt: IndexSet, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsarray/addobserver(_:toobjectsat:forkeypath:options:context:).md)
  Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/removeobserver(_:fromobjectsat:forkeypath:))*