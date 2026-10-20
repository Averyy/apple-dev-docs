# LAError.Code.systemCancel

**Framework**: Local Authentication  
**Kind**: case  
**Role**: Case

The system canceled authentication.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case systemCancel
```

```c
LAErrorSystemCancel
```

#### Discussion

This might happen if another app comes to the foreground while your app displays the authentication dialog.

## See Also

### Cancellation
- [LAError.Code.appCancel](./appcancel.md)
  The app canceled authentication.
- [LAError.Code.userCancel](./usercancel.md)
  The user tapped the cancel button in the authentication dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code/systemcancel)*