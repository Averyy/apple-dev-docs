# touchIDAny

**Framework**: Security  
**Kind**: property

Constraint to access an item with Touch ID for any enrolled fingers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var touchIDAny: SecAccessControlCreateFlags { get }
```

#### Discussion

Touch ID must be available and enrolled with at least one finger. The item is still accessible by Touch ID if fingers are added or removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/touchidany)*