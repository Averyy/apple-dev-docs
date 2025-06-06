# topShelfContentDidChange()

**Framework**: TV Services  
**Kind**: method

Tells the system that your top shelf content changed and requires an update.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class func topShelfContentDidChange()
```

#### Discussion

Call this method when your top shelf content changes. This method notifies the system asynchronously and returns. You may call this method either from your app or from your Top Shelf app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcontentprovider/topshelfcontentdidchange())*