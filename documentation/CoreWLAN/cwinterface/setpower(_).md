# setPower(_:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Sets the interface power state.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setPower(_ power: Bool) throws
```

```objc
- (BOOL) setPower:(BOOL) power error:(NSError **) error;
```

#### Discussion

This operation may require an administrator password.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `power`: A Boolean value corresponding to the power state. *NO* indicates the “OFF” state.

## See Also

### Setting interface parameters
- [func setPairwiseMasterKey(Data?) throws](./setpairwisemasterkey%28_%29.md)
  Sets the interface pairwise primary key (PMK).
- [func setWEPKey(Data?, flags: CWCipherKeyFlags, index: Int) throws](./setwepkey%28_,flags,index%29.md)
  Sets the interface WEP key.
- [func setWLANChannel(CWChannel) throws](./setwlanchannel%28_%29.md)
  Sets the interface channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/setpower(_:))*