# setWLANChannel(_:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Sets the interface channel.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setWLANChannel(_ channel: CWChannel) throws
```

```objc
- (BOOL) setWLANChannel:(CWChannel *) channel error:(NSError **) error;
```

#### Discussion

The channel cannot be changed if the interface is associated to a network.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `channel`: A CWChannel object corresponding to the channel.

## See Also

### Setting interface parameters
- [func setPairwiseMasterKey(Data?) throws](./setpairwisemasterkey%28_%29.md)
  Sets the interface pairwise primary key (PMK).
- [func setPower(Bool) throws](./setpower%28_%29.md)
  Sets the interface power state.
- [func setWEPKey(Data?, flags: CWCipherKeyFlags, index: Int) throws](./setwepkey%28_,flags,index%29.md)
  Sets the interface WEP key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/setwlanchannel(_:))*