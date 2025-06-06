# setPower(_:)

**Framework**: Core WLAN  
**Kind**: method

Sets the interface power state.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setPower(_ power: Bool) throws
```

#### Discussion

This operation may require an administrator password.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `power`: A Boolean value corresponding to the power state.   indicates the “OFF” state.

## See Also

- [func setPairwiseMasterKey(Data?) throws](cwinterface/setpairwisemasterkey(_:).md)
  Sets the interface pairwise primary key (PMK).
- [func setWEPKey(Data?, flags: CWCipherKeyFlags, index: Int) throws](cwinterface/setwepkey(_:flags:index:).md)
  Sets the interface WEP key.
- [func setWLANChannel(CWChannel) throws](cwinterface/setwlanchannel(_:).md)
  Sets the interface channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/setpower(_:))*