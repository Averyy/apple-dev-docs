# removeObserver(_:forKeyPath:context:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeObserver:(NSObject *) observer forKeyPath:(NSString *) keyPath context:(void *) context;
```

## Discussion

`NSOrderedSet` objects are not observable, so this method raises an exception when invoked on an `NSOrderedSet` object. Instead of observing an ordered set, observe the to-many relationship for which the ordered set is the collection of related objects.

## Parameters

- `observer`: The object to remove as an observer.
- `keyPath`: A key-path, relative to the set, for which observer is registered to receive KVO change notifications. This value must not be nil.
- `context`: The context passed to the notifications.

## See Also

### Key-Value Observing Support
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./addobserver%28_,forkeypath,options,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](./removeobserver%28_,forkeypath%29.md)
  Raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/removeobserver(_:forkeypath:context:))*