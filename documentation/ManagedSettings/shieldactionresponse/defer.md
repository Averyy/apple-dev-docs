# ShieldActionResponse.defer

**Framework**: ManagedSettings  
**Kind**: case

An instruction to defer a response to the action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case `defer`
```

#### Discussion

Use `defer` to delay an immediate response to a shield action; for example, if your extension on a client device sends a remote request to a parent or guardian’s device. When you specify this option, the shield redraws its UI, which gives your extension on the client device an opportunity to reconfigure the shield’s appearance.

## See Also

- [ShieldActionResponse.close](shieldactionresponse/close.md)
  An instruction for the system to close the current application or web browser.
- [ShieldActionResponse.none](shieldactionresponse/none.md)
  An instruction that the system doesn’t need to take any additional action on behalf of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldactionresponse/defer)*