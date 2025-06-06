# objectsByEvaluating(withContainers:)

**Framework**: Foundation  
**Kind**: method

Returns the actual object or objects specified by the receiver as evaluated in the context of given container object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func objectsByEvaluating(withContainers containers: Any) -> Any?
```

#### Return Value

The actual object or objects specified by the receiver as evaluated in the context of its container object or objects (`containers`).

#### Discussion

Invokes [`indicesOfObjectsByEvaluating(withContainer:count:)`](nsscriptobjectspecifier/indicesofobjectsbyevaluating(withcontainer:count:).md) on `self` to get an array of pointers to indices of elements in `containers` that have values paired with the message receiver’s key. This method then uses key-value coding to obtain the object or objects associated with the key; it returns these objects or `nil` if there are no matching values in containers. If there are multiple matching values, they are returned in an `NSArray`; if matching values are `nil`, `NSNull` objects are substituted. If `containers` is an `NSArray`, the method recursively evaluates each element in the array and returns an `NSArray` with evaluated objects (including `NSNulls`) in their corresponding slots.

## See Also

- [func indicesOfObjectsByEvaluating(withContainer: Any, count: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Int>?](nsscriptobjectspecifier/indicesofobjectsbyevaluating(withcontainer:count:).md)
  This primitive method must be overridden by subclasses to return a pointer to an array of indices identifying objects in the key of a given container that are identified by the receiver of the message.
- [var objectsByEvaluatingSpecifier: Any?](nsscriptobjectspecifier/objectsbyevaluatingspecifier.md)
  Returns the actual object represented by the nested series of object specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/objectsbyevaluating(withcontainers:))*