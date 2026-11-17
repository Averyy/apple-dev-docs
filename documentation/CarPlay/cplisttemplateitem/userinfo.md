# userInfo

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

App-specific data you associate with the item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var userInfo: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id userInfo;
```

## Discussion

Use this property to attach app-specific data to the item. For example, you might attach the model object from your app that corresponds to the item’s content. This information is just for your app, and CarPlay doesn’t use it. The default value of this property is `nil`.

## See Also

### Managing content
- [var text: String?](./text.md)
  The primary text to display for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplateitem/userinfo)*