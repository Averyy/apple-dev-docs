# addObserver(_:toObjectsAt:forKeyPath:options:context:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.

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
func addObserver(_ observer: NSObject, toObjectsAt indexes: IndexSet, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

```objc
- (void) addObserver:(NSObject *) observer toObjectsAtIndexes:(NSIndexSet *) indexes forKeyPath:(NSString *) keyPath options:(NSKeyValueObservingOptions) options context:(void *) context;
```

#### Discussion

The `options` determine what is included in the notifications, and the `context` is passed in the notifications.

This is not merely a convenience method; invoking this method is potentially much faster than repeatedly invoking [`addObserver(_:forKeyPath:options:context:)`](../../ObjectiveC/nsobject-swift.class/addobserver%28_,forkeypath,options,context%29.md).

## Parameters

- `observer`: The observer.
- `indexes`: The index set.
- `keyPath`: The key path, relative to the array, to be observed.
- `options`: The options to be included in the notification.
- `context`: The context passed to the notifications.

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
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String)](./removeobserver%28_,fromobjectsat,forkeypath%29.md)
  Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/addobserver(_:toobjectsat:forkeypath:options:context:))*