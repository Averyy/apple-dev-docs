# isSIMInserted

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates whether a SIM is present.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
var isSIMInserted: Bool { get }
```

```objc
@property (readonly, getter=isSIMInserted) BOOL SIMInserted;
```

## Discussion

This value property is `true` if the system finds a SIM matching the `Info.plist` carrier information (MCC / MNC / GID1 / GID2).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscriber/issiminserted)*