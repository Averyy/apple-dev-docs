# addObserver(_:forKeyPath:options:context:)

**Framework**: Foundation  
**Kind**: method

Raises an exception.

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
func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

#### Discussion

`NSArray` objects are not observable, so this method raises an exception when invoked on an `NSArray` object. Instead of observing an array, observe the to-many relationship for which the array is the collection of related objects.

## Parameters

- `observer`: The object to register for KVO notifications. The observer must implement the key-value observing method  doc://com.apple.documentation/documentation/objectivec/nsobject/1416553-observevalue .
- `keyPath`: The key path, relative to the array, of the property to observe. This value must not be  .
- `options`: A combination of   values that specifies what is included in observation notifications.
- `context`: Arbitrary data that is passed to   in  doc://com.apple.documentation/documentation/objectivec/nsobject/1416553-observevalue .

## See Also

- [func removeObserver(NSObject, forKeyPath: String)](nsarray/removeobserver(_:forkeypath:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsarray/removeobserver(_:forkeypath:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsarray/removeobserver(_:fromobjectsat:forkeypath:context:).md)
  Raises an exception.
- [func addObserver(NSObject, toObjectsAt: IndexSet, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsarray/addobserver(_:toobjectsat:forkeypath:options:context:).md)
  Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String)](nsarray/removeobserver(_:fromobjectsat:forkeypath:).md)
  Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/addobserver(_:forkeypath:options:context:))*