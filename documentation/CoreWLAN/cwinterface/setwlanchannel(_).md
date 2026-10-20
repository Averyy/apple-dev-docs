# setWLANChannel(_:)

**Framework**: Core WLAN  
**Kind**: method

Sets the interface channel.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setWLANChannel(_ channel: CWChannel) throws
```

#### Discussion

The channel cannot be changed if the interface is associated to a network.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `channel`: A CWChannel object corresponding to the channel.

## See Also

- [func setPairwiseMasterKey(Data?) throws](cwinterface/setpairwisemasterkey(_:).md)
  Sets the interface pairwise primary key (PMK).
- [func setPower(Bool) throws](cwinterface/setpower(_:).md)
  Sets the interface power state.
- [func setWEPKey(Data?, flags: CWCipherKeyFlags, index: Int) throws](cwinterface/setwepkey(_:flags:index:).md)
  Sets the interface WEP key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/setwlanchannel(_:))*