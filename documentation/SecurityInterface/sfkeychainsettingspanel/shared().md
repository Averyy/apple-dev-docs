# shared()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Type Method

Returns a shared keychain settings panel object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class func shared() -> SFKeychainSettingsPanel!
```

```objc
+ (SFKeychainSettingsPanel *) sharedKeychainSettingsPanel;
```

## Discussion

If the shared object has not already been created, this method allocates and initializes the object first.

## See Also

### Related Documentation
- [Keychain Services Programming Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/keychainServConcepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000897)


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsettingspanel/shared())*