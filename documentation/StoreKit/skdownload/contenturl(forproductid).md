# contentURL(forProductID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Returns the local location for the previously downloaded flie.

**Availability**:
- Mac Catalyst 13.0+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
class func contentURL(forProductID productID: String) -> URL?
```

```objc
+ (NSURL *) contentURLForProductID:(NSString *) productID;
```

## Mentions

- [Unlocking purchased content](../unlocking-purchased-content.md)

#### Return Value

The local location for the previously downloaded flie.

#### Discussion

Use this method to locate the content on subsequent launches of your app.

## Parameters

- `productID`: The product identifier.

## See Also

### Managing Downloaded Content
- [class func deleteContent(forProductID: String)](./deletecontent%28forproductid%29.md)
  Deletes the previously downloaded file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/contenturl(forproductid:))*