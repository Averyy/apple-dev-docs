# ILClassificationAction.none

**Framework**: SMS and Call Reporting  
**Kind**: case  
**Role**: Case

No action is required.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
case none
```

```c
ILClassificationActionNone
```

## Discussion

The extension just dismisses the [`ILClassificationUIExtensionViewController`](../../IdentityLookupUI/ilclassificationuiextensionviewcontroller.md).

## See Also

### Classifications
- [ILClassificationAction.reportJunk](./reportjunk.md)
  The system should report the communication as junk.
- [ILClassificationAction.reportJunkAndBlockSender](./reportjunkandblocksender.md)
  The system should report the communication as junk and add the number to the system’s block list.
- [ILClassificationAction.reportNotJunk](./reportnotjunk.md)
  The system should report that the communication is not junk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilclassificationaction/none)*