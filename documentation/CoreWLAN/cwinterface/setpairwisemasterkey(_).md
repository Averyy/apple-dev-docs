# setPairwiseMasterKey(_:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Sets the interface pairwise primary key (PMK).

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setPairwiseMasterKey(_ key: Data?) throws
```

```objc
- (BOOL) setPairwiseMasterKey:(NSData *) key error:(NSError **) error;
```

## Discussion

*key* must be 32 octets. If *key* is *nil*, this method clears the PMK for the interface.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `key`: An NSData object containing the pairwise primary key (PMK).

## See Also

### Setting interface parameters
- [func setPower(Bool) throws](./setpower%28_%29.md)
  Sets the interface power state.
- [func setWEPKey(Data?, flags: CWCipherKeyFlags, index: Int) throws](./setwepkey%28_,flags,index%29.md)
  Sets the interface WEP key.
- [func setWLANChannel(CWChannel) throws](./setwlanchannel%28_%29.md)
  Sets the interface channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/setpairwisemasterkey(_:))*