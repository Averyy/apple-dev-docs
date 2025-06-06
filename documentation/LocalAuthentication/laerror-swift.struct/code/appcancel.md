# LAError.Code.appCancel

**Framework**: Local Authentication  
**Kind**: case

The app canceled authentication.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case appCancel
```

#### Discussion

You receive this error if you call the [`invalidate()`](lacontext/invalidate().md) method while authentication is in process.

## See Also

- [LAError.Code.systemCancel](laerror-swift.struct/code/systemcancel.md)
  The system canceled authentication.
- [LAError.Code.userCancel](laerror-swift.struct/code/usercancel.md)
  The user tapped the cancel button in the authentication dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code/appcancel)*