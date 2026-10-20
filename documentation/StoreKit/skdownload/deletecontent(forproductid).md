# deleteContent(forProductID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Deletes the previously downloaded file.

**Availability**:
- Mac Catalyst 13.0+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
class func deleteContent(forProductID productID: String)
```

```objc
+ (void) deleteContentForProductID:(NSString *) productID;
```

## Mentions

- [Unlocking purchased content](../unlocking-purchased-content.md)

## Parameters

- `productID`: The product identifier.

## See Also

### Managing Downloaded Content
- [class func contentURL(forProductID: String) -> URL?](./contenturl%28forproductid%29.md)
  Returns the local location for the previously downloaded flie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/deletecontent(forproductid:))*