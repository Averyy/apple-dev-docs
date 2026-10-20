# item

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

A reference to the keychain item in which the event occurred. If the event did not involve an item, this field is not valid.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var item: Unmanaged<SecKeychainItem>
```

```c
SecKeychainItemRef item;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincallbackinfo/item)*