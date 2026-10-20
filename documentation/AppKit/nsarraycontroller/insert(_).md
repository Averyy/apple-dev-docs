# insert(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new object and inserts it into the receiver’s content array.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func insert(_ sender: Any?)
```

```objc
- (void) insert:(id) sender;
```

#### Discussion

If an entity name is specified (see [`entityName`](../nsobjectcontroller/entityname.md)), this method creates an instance of the of the class specified by the entity, otherwise this method creates an instance of the class specified by  [`objectClass`](../nsobjectcontroller/objectclass.md).

##### Special Considerations

Beginning with OS X v10.4 the result of this method is deferred until the next iteration of the runloop so that the error presentation mechanism can provide feedback as a sheet.

## Parameters

- `sender`: Typically the object that invoked this method.

## See Also

### Inserting
- [var canInsert: Bool](./caninsert.md)
  Returns a Boolean value that indicates whether an object can be inserted into the receiver’s content collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/insert(_:))*