# TVTopShelfItemsDidChangeNotification

**Framework**: TV Services  
**Kind**: var  
**Role**: Global Variable

A notification to post when your app’s Top Shelf content has changed.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

## Declaration

```c
extern NSString * const TVTopShelfItemsDidChangeNotification;
```

## Discussion

When the content has changed, post a new notification using the default notification center (`[NSNotificationCenter defaultCenter]`). At some point in the future, the system will fetch the new data from your extension. The notification’s parameters are ignored and should be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitemsdidchangenotification)*