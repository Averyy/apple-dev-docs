# setWEPKey(_:flags:index:)

**Framework**: Corewlan  
**Kind**: method

Sets the interface WEP key.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setWEPKey(_ key: Data?, flags: CWCipherKeyFlags, index: Int) throws
```

#### Discussion

 must be 5 octets for WEP-40 or 13 octets for WEP-104. If  is , this method clears the WEP key for the interface.  must correspond to default key index 1-4.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `key`: An NSData object containing the WEP key.
- `flags`: An NSUInteger indicating which cipher key flags to use for the specified key.
- `index`: An NSUInteger indicating which default key index to use for the specified key.

## See Also

- [func setPairwiseMasterKey(Data?) throws](cwinterface/setpairwisemasterkey(_:).md)
  Sets the interface pairwise primary key (PMK).
- [func setPower(Bool) throws](cwinterface/setpower(_:).md)
  Sets the interface power state.
- [func setWLANChannel(CWChannel) throws](cwinterface/setwlanchannel(_:).md)
  Sets the interface channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/setwepkey(_:flags:index:))*