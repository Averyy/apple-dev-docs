# default()

**Framework**: Open Directory  
**Kind**: method  
**Role**: Type Method

Returns a shared instance of the local session.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
class func `default`() -> ODSession!
```

```objc
+ (ODSession *) defaultSession;
```

## Return Value

A shared instance of the local session.

## See Also

### Creating and Accessing Sessions
- [init(options: [AnyHashable : Any]!) throws](./init%28options%29.md)
  Creates a session object directed over proxy to another host.
- [+ sessionWithOptions:error:](./sessionwithoptions_error_.md)
  Returns an autoreleased session object directed over proxy to another host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsession/default())*