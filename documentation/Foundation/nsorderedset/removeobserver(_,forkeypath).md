# removeObserver(_:forKeyPath:)

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
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)
```

#### Discussion

`NSOrderedSet` objects are not observable, so this method raises an exception when invoked on an `NSOrderedSet` object. Instead of observing an ordered set, observe the to-many relationship for which the ordered set is the collection of related objects.

## Parameters

- `observer`: The object to remove as an observer.
- `keyPath`: A key-path, relative to the set, for which observer is registered to receive KVO change notifications. This value must not be nil.

## See Also

- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsorderedset/addobserver(_:forkeypath:options:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsorderedset/removeobserver(_:forkeypath:context:).md)
  Raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/removeobserver(_:forkeypath:))*