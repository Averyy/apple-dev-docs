# handler

**Framework**: CarPlay  
**Kind**: property  
**Required**: Yes

An optional closure that CarPlay invokes when the user selects the list item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var handler: ((any CPSelectableListItem, @escaping () -> Void) -> Void)? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpselectablelistitem/handler)*