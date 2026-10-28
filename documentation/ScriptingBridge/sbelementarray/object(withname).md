# object(withName:)

**Framework**: Scripting Bridge  
**Kind**: method  
**Role**: Instance Method

Returns the object in the array with the given name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func object(withName name: String) -> Any
```

```objc
- (ObjectType) objectWithName:(NSString *) name;
```

## Return Value

A reference to the designated object or `nil` if the object couldn’t be found.

## Discussion

This method is provided as an alternative to [`object(at:)`](../../Foundation/nsarray/object%28at%29.md) for applications where a name is available instead of (or in addition to) an index. A name is generally more stable than an index. For example, it is typically more useful to identify a mailbox in Mail by its name than by its index in the list of mailboxes.

## Parameters

- `name`: The name of one of the receiver’s objects.

## See Also

### Getting Objects in the Array
- [func object(withID: Any) -> Any](./object%28withid%29.md)
  Returns the object in the array with the given identifier.
- [func object(atLocation: Any) -> Any](./object%28atlocation%29.md)
  Returns the object at the given location in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/object(withname:))*