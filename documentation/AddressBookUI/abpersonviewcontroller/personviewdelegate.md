# personViewDelegate

**Framework**: Address Book UI  
**Kind**: property

The person-view controller delegate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
unowned(unsafe) var personViewDelegate: (any ABPersonViewControllerDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`ABPersonViewControllerDelegate`](abpersonviewcontrollerdelegate.md) protocol.

## See Also

- [protocol ABPersonViewControllerDelegate](abpersonviewcontrollerdelegate.md)
  The `ABPersonViewControllerDelegate` protocol declares the interface that must be implemented by [`ABPersonViewController`](abpersonviewcontroller.md) delegates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/personviewdelegate)*