# perform(withItems:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Manually performs the service on the provided items.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func perform(withItems items: [Any])
```

```objc
- (void) performWithItems:(NSArray *) items;
```

#### Discussion

In most cases this will display a sharing window.

## Parameters

- `items`: The items to share.

## See Also

### Related Documentation
- [func canPerform(withItems: [Any]?) -> Bool](./canperform%28withitems%29.md)
  Returns whether the service can share all the specified items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/perform(withitems:))*