# removeObserver(_:forKeyPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)
```

```objc
- (void) removeObserver:(NSObject *) observer forKeyPath:(NSString *) keyPath;
```

## Discussion

`NSArray` objects are not observable, so this method raises an exception when invoked on an `NSArray` object. Instead of observing an array, observe the to-many relationship for which the array is the collection of related objects.

## Parameters

- `observer`: The object to remove as an observer.
- `keyPath`: A key-path, relative to the array, for which `observer` is registered to receive KVO change notifications. This value must not be `nil`.

## See Also

### Key-Value Observing
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./addobserver%28_,forkeypath,options,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](./removeobserver%28_,forkeypath,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String, context: UnsafeMutableRawPointer?)](./removeobserver%28_,fromobjectsat,forkeypath,context%29.md)
  Raises an exception.
- [func addObserver(NSObject, toObjectsAt: IndexSet, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./addobserver%28_,toobjectsat,forkeypath,options,context%29.md)
  Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String)](./removeobserver%28_,fromobjectsat,forkeypath%29.md)
  Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/removeobserver(_:forkeypath:))*