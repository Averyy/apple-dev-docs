# newPersonViewDelegate

**Framework**: Address Book UI  
**Kind**: property

The delegate of a new-person view controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
unowned(unsafe) var newPersonViewDelegate: (any ABNewPersonViewControllerDelegate)? { get set }
```

## See Also

- [protocol ABNewPersonViewControllerDelegate](abnewpersonviewcontrollerdelegate.md)
  The `ABNewPersonViewControllerDelegate` protocol declares the interface that [`ABNewPersonViewController`](abnewpersonviewcontroller.md) delegates must implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/newpersonviewdelegate)*