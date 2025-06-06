# object(atLocation:)

**Framework**: Scripting Bridge  
**Kind**: method

Returns the object at the given location in the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func object(atLocation location: Any) -> Any
```

#### Return Value

A reference to the [`SBObject`](sbobject.md) object identified by `loc` or `nil` if the object couldn’t be located.

#### Discussion

This method is a generalization of [`objectAtIndex:`](https://developer.apple.com/documentation/foundation/nsarray/1417555-objectatindex) for applications where the “index” is not simply an integer. For example, Finder can specify objects using a [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object as a location. In OSA this is known as “absolute position,” a generalization of the notion of “index” in Foundation—it could be an integer, but it doesn’t have to be. A single object may even have a number of different “absolute position” values depending on the container.

## See Also

- [func object(withName: String) -> Any](sbelementarray/object(withname:).md)
  Returns the object in the array with the given name.
- [func object(withID: Any) -> Any](sbelementarray/object(withid:).md)
  Returns the object in the array with the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/object(atlocation:))*