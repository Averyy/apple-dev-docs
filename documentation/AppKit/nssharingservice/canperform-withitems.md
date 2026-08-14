# canPerform(withItems:)

**Framework**: AppKit  
**Kind**: method

Returns whether the service can share all the specified items.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func canPerform(withItems items: [Any]?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the service can share all the items; [`false`](https://developer.apple.com/documentation/swift/false) otherwise. If `items` is `nil`, the method will return [`true`](https://developer.apple.com/documentation/swift/true) when the service is configured.

#### Discussion

This method can be used to validate a custom user interface such as a dedicated Twitter button.  Therefore you could call it once at launch time with `nil` items to check whether to display the button or not, and then with real items to enable and disable the button depending on the context or selection.

## Parameters

- `items`: The items to share.

## See Also

- [func perform(withItems: [Any])](nssharingservice/perform(withitems:).md)
  Manually performs the service on the provided items.
- [class func sharingServices(forItems: [Any]) -> [NSSharingService]](nssharingservice/sharingservices(foritems:).md)
  Returns a list of sharing services which could share all the provided items together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/canperform(withitems:))*