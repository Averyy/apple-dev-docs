# contentURL(forProductID:)

**Framework**: StoreKit  
**Kind**: method

Returns the local location for the previously downloaded flie.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.8+

## Declaration

```swift
class func contentURL(forProductID productID: String) -> URL?
```

## Mentions

- [Unlocking purchased content](unlocking-purchased-content.md)

#### Return Value

The local location for the previously downloaded flie.

#### Discussion

Use this method to locate the content on subsequent launches of your app.

## Parameters

- `productID`: The product identifier.

## See Also

- [class func deleteContent(forProductID: String)](skdownload/deletecontent(forproductid:).md)
  Deletes the previously downloaded file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/contenturl(forproductid:))*