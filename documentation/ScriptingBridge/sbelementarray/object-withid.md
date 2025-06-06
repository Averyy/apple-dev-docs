# object(withID:)

**Framework**: Scripting Bridge  
**Kind**: method

Returns the object in the array with the given identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func object(withID identifier: Any) -> Any
```

#### Return Value

A reference to the identified object or `nil` if could not be found.

#### Discussion

This method is provided as an alternative to [`objectAtIndex:`](https://developer.apple.com/documentation/foundation/nsarray/1417555-objectatindex) for applications where an identifier is available instead of (or in addition to) an index. A unique ID is generally more stable than an index. For example, it may be more useful to identify a contact in Address Book by its identifier (which doesn’t change over time) than by its index in the list of contacts (which can change as contacts are added or removed).

## Parameters

- `identifier`: The identifier of one of the receiver’s objects.

## See Also

- [func object(withName: String) -> Any](sbelementarray/object(withname:).md)
  Returns the object in the array with the given name.
- [func object(atLocation: Any) -> Any](sbelementarray/object(atlocation:).md)
  Returns the object at the given location in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/object(withid:))*