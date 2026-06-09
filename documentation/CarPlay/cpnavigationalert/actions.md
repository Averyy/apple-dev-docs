# actions

**Framework**: CarPlay  
**Kind**: property

The array of actions associated with this navigation alert.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var actions: [CPAlertAction] { get }
```

#### Discussion

If the alert was created with the older @c primaryAction / @c secondaryAction initializer, this property returns those actions as an array for backward compatibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/actions)*