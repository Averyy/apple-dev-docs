# object(withName:)

**Framework**: Scripting Bridge  
**Kind**: method

Returns the object in the array with the given name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func object(withName name: String) -> Any
```

#### Return Value

A reference to the designated object or `nil` if the object couldn’t be found.

#### Discussion

This method is provided as an alternative to [`objectAtIndex:`](https://developer.apple.com/documentation/foundation/nsarray/1417555-objectatindex) for applications where a name is available instead of (or in addition to) an index. A name is generally more stable than an index. For example, it is typically more useful to identify a mailbox in Mail by its name than by its index in the list of mailboxes.

## Parameters

- `name`: The name of one of the receiver’s objects.

## See Also

- [func object(withID: Any) -> Any](sbelementarray/object(withid:).md)
  Returns the object in the array with the given identifier.
- [func object(atLocation: Any) -> Any](sbelementarray/object(atlocation:).md)
  Returns the object at the given location in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/object(withname:))*