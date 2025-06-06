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

`NSOrderedSet` objects are not observable, so this method raises an exception when invoked on an `NSOrderedSet` object. Instead of observing an ordered set, observe the to-many relationship for which the ordered set is the collection of related objects.

## Parameters

- `observer`: The object to register for KVO notifications.
- `keyPath`: The key path, relative to the array, of the property to observe. This value must not be nil.
- `options`: A combination of   values that specifies what is included in observation notifications.
- `context`: Arbitrary data that is passed to observer in  .

## See Also

- [func removeObserver(NSObject, forKeyPath: String)](nsorderedset/removeobserver(_:forkeypath:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsorderedset/removeobserver(_:forkeypath:context:).md)
  Raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/addobserver(_:forkeypath:options:context:))*