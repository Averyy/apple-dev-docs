# sessionWithOptions:error:

**Framework**: Open Directory  
**Kind**: method  
**Role**: Type Method

Returns an autoreleased session object directed over proxy to another host.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```objc
+ (instancetype) sessionWithOptions:(NSDictionary *) inOptions error:(NSError **) outError;
```

#### Return Value

The initialized session object.

## Parameters

- `inOptions`: A dictionary of options to associate with the session. Can be `nil`.
- `outError`: An error reference for error details. Can be `nil`.

## See Also

### Related Documentation
- [class ODSession](../odsession.md)
  An `ODSession` object serves as a Cocoa wrapper for an Open Directory session.
### Creating and Accessing Sessions
- [class func `default`() -> ODSession!](./default%28%29.md)
  Returns a shared instance of the local session.
- [init(options: [AnyHashable : Any]!) throws](./init%28options%29.md)
  Creates a session object directed over proxy to another host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsession/sessionwithoptions:error:)*