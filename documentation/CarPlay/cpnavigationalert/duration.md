# duration

**Framework**: CarPlay  
**Kind**: property

The amount of time, in seconds, that the alert is visible.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var duration: TimeInterval { get }
```

#### Discussion

Set `duration` to zero to display the alert until dismissed by the user. When `duration` is not zero, [`CPNavigationAlertMinimumDuration`](cpnavigationalertminimumduration.md) determines the minimum amount of time the alert is visible.

## See Also

- [let CPNavigationAlertMinimumDuration: TimeInterval](cpnavigationalertminimumduration.md)
  A constant that defines the minimum amount of time that an alert is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/duration)*