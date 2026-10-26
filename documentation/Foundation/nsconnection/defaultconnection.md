# defaultConnection

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the default `NSConnection` object for the current thread.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Create individual connection instances as needed instead.

## Declaration

```objc
+ (NSConnection *) defaultConnection;
```

#### Return Value

The default `NSConnection` object for the current thread, creating it if necessary.

#### Discussion

The default `NSConnection` object uses a single `NSPort` object for both receiving and sending and is useful only for vending an object; use the [`rootObject`](./rootobject-c.property.md) and [`registerName:`](./registername_.md) methods to do this.

##### Special Considerations

The singleton method of `NSConnection` has been deprecated. It was difficult to ensure that the shared connection wasn’t being used by other operations on the thread on which the default connection was requested. Using `[NSConnection new]` ensures that you get a unique connection object, preventing such collisions.

## See Also

### Related Documentation
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/defaultconnection)*