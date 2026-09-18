# userInfo

**Framework**: CarPlay  
**Kind**: property

Custom information you want to store with the item.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var userInfo: Any? { get set }
```

#### Discussion

Store any app-specific data for the item in this property. For example, you might store a dictionary of keys and values. The item maintains a strong reference to the object you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanelitem/userinfo)*