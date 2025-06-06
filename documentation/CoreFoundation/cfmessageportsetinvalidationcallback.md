# CFMessagePortSetInvalidationCallBack(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the callback function invoked when a CFMessagePort object is invalidated.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFMessagePortSetInvalidationCallBack(_ ms: CFMessagePort!, _ callout: CFMessagePortInvalidationCallBack!)
```

#### Discussion

If `ms` is already invalid, `callout` is invoked immediately.

## Parameters

- `ms`: The message port to examine.
- `callout`: The callback function to invoke when   is invalidated. Pass   to remove a callback.

## See Also

- [func CFMessagePortCreateRunLoopSource(CFAllocator!, CFMessagePort!, CFIndex) -> CFRunLoopSource!](cfmessageportcreaterunloopsource(_:_:_:).md)
  Creates a CFRunLoopSource object for a CFMessagePort object.
- [func CFMessagePortSetName(CFMessagePort!, CFString!) -> Bool](cfmessageportsetname(_:_:).md)
  Sets the name of a local CFMessagePort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportsetinvalidationcallback(_:_:))*