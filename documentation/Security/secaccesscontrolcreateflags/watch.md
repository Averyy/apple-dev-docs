# watch

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

Constraint to access an item with a watch.

**Availability**:
- macOS 10.15+ - Deprecated in 15.0 (renamed: SecAccessControlCreateFlags.companion)

## Declaration

```swift
static var watch: SecAccessControlCreateFlags { get }
```

```c
kSecAccessControlWatch
```

## Discussion

The system attempts to locate a nearby, paired Apple Watch running watchOS 6 or later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/watch)*