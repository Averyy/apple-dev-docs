# nodeWithSession:type:error:

**Framework**: Open Directory  
**Kind**: method  
**Role**: Type Method

Returns an autoreleased node object with a specified session and type.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```objc
+ (instancetype) nodeWithSession:(ODSession *) inSession type:(ODNodeType) inType error:(NSError **) outError;
```

## Return Value

The created node object.

## Parameters

- `inSession`: The session.
- `inType`: The node type.
- `outError`: An error reference for error details. Can be `nil`.

## See Also

### Creating and Initializing a Node
- [init(session: ODSession!, name: String!) throws](./init%28session,name%29.md)
  Creates a node object with a specified session and name.
- [init(session: ODSession!, type: ODNodeType) throws](./init%28session,type%29.md)
  Creates a node object with a specified session and type.
- [+ nodeWithSession:name:error:](./nodewithsession_name_error_.md)
  Returns an autoreleased node object with a specified session and name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/nodewithsession:type:error:)*