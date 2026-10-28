# userInfo

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An opaque value for the list item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var userInfo: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id userInfo;
```

## Discussion

Use this property to attach a value that provides additional context to the list item. For example, you can attach a model object and reference it in the list item’s [`handler`](./handler.md) when processing the selection.

## See Also

### Managing Configuration
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates if the item is enabled.
- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](./handler.md)
  An optional closure that CarPlay invokes when the user selects the list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/userinfo)*