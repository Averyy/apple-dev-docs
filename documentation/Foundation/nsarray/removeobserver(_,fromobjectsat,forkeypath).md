# removeObserver(_:fromObjectsAt:forKeyPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeObserver:(NSObject *) observer fromObjectsAtIndexes:(NSIndexSet *) indexes forKeyPath:(NSString *) keyPath;
```

#### Discussion

This is not merely a convenience method; invoking this method is potentially much faster than repeatedly invoking [`removeObserver(_:forKeyPath:)`](../../ObjectiveC/nsobject-swift.class/removeobserver%28_,forkeypath%29.md).

## Parameters

- `observer`: The observer.
- `indexes`: The index set.
- `keyPath`: The key path, relative to the array, to be observed.

## See Also

### Key-Value Observing
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./addobserver%28_,forkeypath,options,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](./removeobserver%28_,forkeypath%29.md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](./removeobserver%28_,forkeypath,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String, context: UnsafeMutableRawPointer?)](./removeobserver%28_,fromobjectsat,forkeypath,context%29.md)
  Raises an exception.
- [func addObserver(NSObject, toObjectsAt: IndexSet, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./addobserver%28_,toobjectsat,forkeypath,options,context%29.md)
  Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/removeobserver(_:fromobjectsat:forkeypath:))*