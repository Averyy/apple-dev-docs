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

`NSSet` objects are not observable, so this method raises an exception when invoked on an `NSSet` object. Instead of observing a set, observe the unordered to-many relationship for which the set is the collection of related objects.

## Parameters

- `observer`: The object to remove as an observer.
- `keyPath`: A key-path, relative to the set, for which `observer` is registered to receive KVO change notifications. This value must not be `nil`.

## See Also

### Key-Value Observing
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./addobserver%28_,forkeypath,options,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](./removeobserver%28_,forkeypath,context%29.md)
  Raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/removeobserver(_:forkeypath:))*