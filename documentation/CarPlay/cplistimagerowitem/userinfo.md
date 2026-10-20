# userInfo

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An opaque value for the list item.

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

#### Discussion

Use this property to attach a value that provides additional context to the list item. For example, you can attach a model object and reference it in the list item’s [`handler`](./handler.md) or [`listImageRowHandler`](./listimagerowhandler.md) when processing either selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/userinfo)*