# objectClass

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object class to use when creating new objects.

**Availability**:
- macOS

## Declaration

```swift
var objectClass: AnyClass! { get set }
```

```objc
@property (assign, null_resettable) Class objectClass;
```

## Discussion

`NSObjectController`’s default implementation assumes that instances of `objectClass` are initialized using a standard `init` method that takes no arguments.

## See Also

### Related Documentation
- [var managedObjectContext: NSManagedObjectContext?](./managedobjectcontext.md)
  The receiver’s managed object context.
- [var entityName: String?](./entityname.md)
  The entity name used by the receiver to create new objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/objectclass)*