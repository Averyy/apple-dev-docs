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

`NSSet` objects are not observable, so this method raises an exception when invoked on an `NSSet` object. Instead of observing a set, observe the unordered to-many relationship for which the set is the collection of related objects.

## Parameters

- `observer`: The object to remove as an observer.
- `keyPath`: A key-path, relative to the set, for which   is registered to receive KVO change notifications. This value must not be  .
- `context`: Arbitrary data that is passed to   in  doc://com.apple.documentation/documentation/objectivec/nsobject/1416553-observevalue .

## See Also

- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsset/addobserver(_:forkeypath:options:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](nsset/removeobserver(_:forkeypath:).md)
  Raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/removeobserver(_:forkeypath:context:))*