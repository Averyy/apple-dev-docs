# isAttributeWanted(_:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

A method that indicates whether the request wants given attribute.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func isAttributeWanted(_ attribute: FSItem.Attribute) -> Bool
```

```objc
- (BOOL) isAttributeWanted:(FSItemAttribute) attribute;
```

## Parameters

- `attribute`: The [`FSItem.Attribute`](../attribute.md) to check.

## See Also

### Inspecting requested attributes
- [var wantedAttributes: FSItem.Attribute](./wantedattributes.md)
  The attributes requested by the request.
- [FSItem.Attribute](../attribute.md)
  A value that indicates a set of item attributes to get or set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/getattributesrequest/isattributewanted(_:))*