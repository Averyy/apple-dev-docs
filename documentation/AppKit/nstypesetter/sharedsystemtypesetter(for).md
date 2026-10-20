# sharedSystemTypesetter(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a shared instance of a reentrant typesetter that implements typesetting with the specified behavior.

**Availability**:
- macOS

## Declaration

```swift
class func sharedSystemTypesetter(for behavior: NSLayoutManager.TypesetterBehavior) -> Any
```

```objc
+ (id) sharedSystemTypesetterForBehavior:(NSTypesetterBehavior) behavior;
```

#### Return Value

A shared instance of a reentrant typesetter that implements typesetting with the specified behavior.

#### Discussion

Possible return values are described in the [`NSLayoutManager.TypesetterBehavior`](../nslayoutmanager/typesetterbehavior-swift.enum.md) section for [`NSLayoutManager`](../nslayoutmanager.md).

## Parameters

- `behavior`: The desired behavior.

## See Also

### Related Documentation
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](./typesetterbehavior.md)
  Returns the current typesetter behavior.
### Getting a typesetter
- [class var sharedSystemTypesetter: NSTypesetter](./sharedsystemtypesetter.md)
  Returns a shared instance of a reentrant typesetter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/sharedsystemtypesetter(for:))*