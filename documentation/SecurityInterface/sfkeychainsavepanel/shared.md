# shared()

**Framework**: Security Interface  
**Kind**: method

Returns a shared keychain save panel object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class func shared() -> SFKeychainSavePanel!
```

#### Discussion

If the shared object has not already been created, this method allocates and initializes the object first.

## See Also

- [Keychain Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/keychainServConcepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000897)


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel/shared())*