# setWEPKey(_:flags:index:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Sets the interface WEP key.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setWEPKey(_ key: Data?, flags: CWCipherKeyFlags, index: Int) throws
```

```objc
- (BOOL) setWEPKey:(NSData *) key flags:(CWCipherKeyFlags) flags index:(NSInteger) index error:(NSError **) error;
```

#### Discussion

*key* must be 5 octets for WEP-40 or 13 octets for WEP-104. If *key* is *nil*, this method clears the WEP key for the interface. *index* must correspond to default key index 1-4.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `key`: An NSData object containing the WEP key.
- `flags`: An NSUInteger indicating which cipher key flags to use for the specified key.
- `index`: An NSUInteger indicating which default key index to use for the specified key.

## See Also

### Setting interface parameters
- [func setPairwiseMasterKey(Data?) throws](./setpairwisemasterkey%28_%29.md)
  Sets the interface pairwise primary key (PMK).
- [func setPower(Bool) throws](./setpower%28_%29.md)
  Sets the interface power state.
- [func setWLANChannel(CWChannel) throws](./setwlanchannel%28_%29.md)
  Sets the interface channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/setwepkey(_:flags:index:))*