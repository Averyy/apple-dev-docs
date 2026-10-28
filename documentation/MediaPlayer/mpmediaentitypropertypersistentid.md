# MPMediaEntityPropertyPersistentID

**Framework**: Media Player  
**Kind**: var  
**Role**: Global Variable

The persistent identifier for a media entity.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let MPMediaEntityPropertyPersistentID: String
```

```c
extern NSString * const MPMediaEntityPropertyPersistentID;
```

## Discussion

This value contains a [`uint64_t`](../kernel/uint64_t.md) (unsigned long long) which you can use to build a media property predicate, as described in [`MPMediaPropertyPredicate`](./mpmediapropertypredicate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaentitypropertypersistentid)*