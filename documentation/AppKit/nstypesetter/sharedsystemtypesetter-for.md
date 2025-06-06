# sharedSystemTypesetter(for:)

**Framework**: AppKit  
**Kind**: method

Returns a shared instance of a reentrant typesetter that implements typesetting with the specified behavior.

**Availability**:
- macOS ?+

## Declaration

```swift
class func sharedSystemTypesetter(for behavior: NSLayoutManager.TypesetterBehavior) -> Any
```

#### Return Value

A shared instance of a reentrant typesetter that implements typesetting with the specified behavior.

#### Discussion

Possible return values are described in the [`NSLayoutManager.TypesetterBehavior`](nslayoutmanager/typesetterbehavior-swift.enum.md) section for [`NSLayoutManager`](nslayoutmanager.md).

## Parameters

- `behavior`: The desired behavior.

## See Also

- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](nstypesetter/typesetterbehavior.md)
  Returns the current typesetter behavior.
- [class var sharedSystemTypesetter: NSTypesetter](nstypesetter/sharedsystemtypesetter.md)
  Returns a shared instance of a reentrant typesetter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/sharedsystemtypesetter(for:))*